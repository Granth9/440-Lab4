# Project Two — Mini Coding Agent Skills

This project adds folder skills to [Mini-Coding-Agent](https://github.com/rasbt/mini-coding-agent).

## Setup

Use Python 3.10 or newer and install [Ollama](https://ollama.com/download). Run
`ollama serve` in one terminal, then run `ollama pull qwen3.5:4b` in another.
The agent runs directly with Python and uses the standard library.

## Component 7 — Agent skills

The agent discovers folder skills before each turn, scores the request against
their triggers, and adds the selected Markdown instructions to the model's
context. The model can also call `use_skill` by name mid-turn. Shell and file
operations still go through the normal tool approval flow.

| Path | Purpose |
| --- | --- |
| `agent_skills.py` | Folder discovery, trigger similarity, and JSONL audit |
| `mini_coding_agent.py` | CLI, model prompt, and tool-loop integration |
| `skill/rl-hyperparams/SKILL.md` | Original Lab 5 skill with a Lab 4 workflow |
| `demo/` | Lab 4 workspace preparation and run evidence |
| `intend.md`, `spec.md`, `plan.md` | SDLC documents |

### Add a skill

Create `skill/pr-review/SKILL.md` in the working directory or at the repository root.

```markdown
Triggers: review a pull request, inspect a diff

# Pull request review

Read the changed files and report correctness regressions with file references.
```

The folder name is the skill ID. `skills/` is also supported, as is an explicit
catalog via `--skills-dir`. Matching normalizes case and punctuation. Exact
trigger phrases score 1.0. Otherwise the agent computes binary-token cosine
similarity and auto-activates a unique winner at or above 0.65. The model sees
the skill names and triggers and can request a skill when automatic matching
finds no winner. Use skill catalogs you trust, since their Markdown becomes
model context for the turn.

### Run the Lab 4 demo

From this project folder, use local clones of the Lab 4 and AIMA repositories listed in
`repo_link.txt`. The preparation command reads pinned revisions and copies
the original lab scripts and four AIMA source files into a fresh workspace.

```bash
lab4_workspace="$(mktemp -d)/lab4"
python3 demo/prepare_lab4.py .. ../../aima-python "$lab4_workspace"
python3 mini_coding_agent.py --cwd "$lab4_workspace" --skills-dir "$PWD/skill" \
  --approval ask --max-steps 10 --max-new-tokens 1500 \
  "Solve Lab 4 using the skill. Run both strategy demonstrations, inspect the AIMA MDP defaults, and write lab4_report.md with the results and Lab 5 comparison."
```

Approve the two lab script commands and the write to `lab4_report.md` when asked.
The Lab 4 scripts demonstrate context engineering and the Lab 5 skill supplies
the reinforcement-learning defaults for comparison with AIMA.

```bash
cat "$lab4_workspace"/.mini-coding-agent/skills/*.jsonl
cat "$lab4_workspace"/lab4_report.md
```

The JSONL events are `prompt`, `similarity_check`, `skill_executed`, and
`skill_request` when the model calls the tool. Each has a session ID and turn ID.
A `skill_executed` entry records that the model responded to a request containing the instructions. See
`.mini-coding-agent/sessions/<session-id>.json` for shell output and the final
response. Logs contain the original prompts and local paths.

The [verified walkthrough](demo/lab4_report.md) includes an actual
[Ollama session](demo/evidence/session.json) and its [skills audit](demo/evidence/skills.jsonl).
The smaller `qwen2.5-coder:1.5b` run needed follow-up prompts to run Strategy 4
and inspect the MDP source. The report explains which results were verified.
Local paths are represented by project-relative paths and a workspace placeholder
in those copies.
