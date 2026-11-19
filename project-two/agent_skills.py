"""Discover folder skills, match requests, and audit skill activation."""

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from math import sqrt
from pathlib import Path

MATCH_THRESHOLD = 0.65
MAX_SKILL_BYTES = 16_000
SKILL_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
TRIGGERS = re.compile(r"^Triggers:[ \t]*(.+)$", re.MULTILINE | re.IGNORECASE)


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


@dataclass(frozen=True)
class Skill:
    name: str
    path: Path
    triggers: tuple[str, ...]
    instructions: str

    def score(self, prompt):
        words = tokens(prompt)
        prompt_terms = set(words)
        normalized = " " + " ".join(words) + " "
        best = 0.0
        for phrase in (self.name, *self.triggers):
            phrase_words = tokens(phrase)
            if not phrase_words:
                continue
            if " " + " ".join(phrase_words) + " " in normalized:
                return 1.0
            terms = set(phrase_words)
            overlap = terms & prompt_terms
            if len(overlap) >= 2:
                best = max(best, len(overlap) / sqrt(len(terms) * len(prompt_terms)))
        return best


class SkillRegistry:
    def __init__(self, roots):
        self.skills = {}
        self.errors = []
        for root in roots:
            if root.is_symlink() or not root.is_dir():
                continue
            for folder in sorted(root.iterdir()):
                if not SKILL_ID.fullmatch(folder.name) or folder.is_symlink() or not folder.is_dir():
                    continue
                for path in sorted(folder.iterdir()):
                    if path.name.casefold() != "skill.md" or path.is_symlink() or not path.is_file():
                        continue
                    try:
                        with path.open("rb") as handle:
                            data = handle.read(MAX_SKILL_BYTES + 1)
                        if len(data) > MAX_SKILL_BYTES:
                            raise ValueError(f"exceeds {MAX_SKILL_BYTES} bytes")
                        text = data.decode("utf-8")
                        instructions = TRIGGERS.sub("", text, count=1).strip()
                        if not instructions:
                            raise ValueError("missing instructions")
                    except (OSError, ValueError) as exc:
                        self.errors.append({"path": str(path), "error": str(exc)})
                        continue
                    metadata = TRIGGERS.search(text)
                    phrases = metadata[1].split(",") if metadata else ()
                    triggers = tuple(phrase.strip() for phrase in phrases if phrase.strip())
                    self.skills.setdefault(folder.name, Skill(folder.name, path, triggers, instructions))
                    break

    def match(self, prompt):
        scores = {name: skill.score(prompt) for name, skill in self.skills.items()}
        ranked = sorted(scores, key=scores.get, reverse=True)
        if not ranked or scores[ranked[0]] < MATCH_THRESHOLD:
            return scores, None, "below_threshold" if ranked else "empty_catalog"
        if len(ranked) > 1 and scores[ranked[0]] == scores[ranked[1]]:
            return scores, None, "ambiguous"
        return scores, ranked[0], "matched"

    def catalog(self):
        return "\n".join(
            f"- {skill.name}: {', '.join(skill.triggers) or skill.name}"
            for skill in self.skills.values()
        )


def audit_event(log_path, session_id, turn_id, event, **details):
    row = {
        "time": datetime.now(timezone.utc).isoformat(),
        "session_id": session_id,
        "turn_id": turn_id,
        "event": event,
        **details,
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row) + "\n")
