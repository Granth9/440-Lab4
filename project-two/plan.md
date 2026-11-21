# Implementation and verification plan

1. Identify the upstream prompt builder, tool loop, and session store. Pin the original lab revisions used in the demonstration.
2. Implement the folder registry, scoring, and append-only session audit. Integrate automatic selection at the start of a turn and add the `use_skill` tool.
3. Convert the Lab 5 skill into the folder layout and add instructions for applying its defaults during a Lab 4 review. Prepare a disposable workspace with the original Lab 4 demos and four AIMA files.
4. Exercise the Lab 4 prompt through the CLI with Ollama and save the report and supporting evidence.
5. Document the setup and record a presentation showing the design, a fresh run, and the report and log.
## Final Verification

The following functionality was verified during development:

- Skill folders are discovered through the registry.
- Skill instructions are loaded from SKILL.md files.
- Similarity scores are calculated against user prompts.
- Matching skills are automatically activated.
- The agent can request additional skills through use_skill.
- Skill instructions are included in subsequent model prompts.
- Prompt, similarity_check, skill_request, and skill_executed
  events are recorded in JSONL logs.
- Both Lab 4 strategy demonstrations execute successfully.
- The Lab 5 reinforcement-learning skill provides the
  hyperparameters used for comparison with AIMA.

### Remaining Submission Verification

Before submission:
- Run the agent with Ollama using a fresh workspace.
- Verify that the agent creates lab4_report.md.
- Verify automatic and mid-turn skill activation.
- Review the generated audit logs.
- Record the required project demonstration video.