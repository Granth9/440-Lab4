# Specification

## Discovery and selection

- Search `skill/` and `skills/` in the working directory and the repository root for direct child folders containing a case-insensitive `SKILL.md` filename. Folder IDs use lowercase ASCII alphanumerics and hyphens. A supplied `--skills-dir` adds a higher-priority catalog.
- An optional `Triggers:` line lists comma-separated phrases. The folder ID is always a trigger. Markdown content below or around the metadata supplies instructions. Skills must contain UTF-8 instructions and fit within 16,000 bytes. Invalid files are skipped and reported in the similarity event.
- For each skill, score its strongest trigger. An exact normalized token phrase scores 1.0. Otherwise use binary-token cosine similarity with at least two shared words. A unique winner at or above 0.65 activates automatically. A tie or low score leaves selection to the model.
- Show the catalog in each model prompt. The model can call `use_skill` by exact registered ID. Inject active instructions in every model prompt for that turn. Clear active skills when a new turn begins. Keep writes and shell calls subject to the original approval rules.

## Audit

Each session writes a JSON Lines file under `.mini-coding-agent/skills/`. A prompt event records the user's text, and a similarity event records every candidate score, the threshold, and the decision. A tool request records the ID and whether it exists. A skill execution event records the skill ID, file path, and activation route after the model responds to the first request containing the instructions. Use the companion session transcript to verify tool results and the final response.

## Acceptance

A folder skill works before the first model step and through a mid-turn tool call. Unrelated and ambiguous prompts produce logged decisions. The Lab 5 skill remains recognizable, and the Lab 4 report cites the persistent context, the isolated contexts, and the AIMA implementation.
