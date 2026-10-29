# Research Context

Strategy 4 in the course slides is Isolation via Sub-Agents:
- A main agent/orchestrator receives a complex task and divides it.
- A context filter prevents full history from leaking into sub-agents.
- Specialized sub-agents receive only context relevant to their task.
- Example roles include code reviewer and researcher.
- The orchestrator combines their outputs.

This Python demo uses separate functions as deterministic stand-ins to demonstrate the architecture without a model API. If the assignment requires LLM-backed agents, these functions would need to be replaced with calls to the required model/API while preserving context filtering.
