# Project Context

This repository contains the AIMA Python project used for CS440 work and two context-engineering demonstrations.

## Repository layout
- `aima-python/`: original AIMA code, including vacuum-agent examples, a grid vacuum environment, and grid MDP examples.
- `strategy_1/`: persistent context files and a Python loader.
- `strategy_4/`: a Python demonstration of orchestrated sub-agents with filtered context.

## Current lab goal
Demonstrate:
1. Persistent context: keep reusable project instructions and notes in files and load them consistently.
2. Isolation via sub-agents: delegate distinct tasks and give each sub-agent only its relevant context.

The current Strategy 4 agents are deterministic Python stand-ins, not LLM-powered agents. Do not describe them as real model-based agents.
