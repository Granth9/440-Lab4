"""Specialized code-review sub-agent (rule-based demo)."""
from typing import Dict, List

def review(context: Dict[str, str], source_files: Dict[str, str]) -> str:
    """Review only the source files and context explicitly passed to this agent."""
    findings: List[str] = []
    env_code = source_files.get("vacuum_env.py", "")
    q_code = source_files.get("q_learning.py", "")
    main_code = source_files.get("main.py", "")

    if not env_code:
        findings.append("No vacuum_env.py content was provided; environment behavior could not be checked.")
    else:
        if "GRID" in env_code and "-1" in env_code:
            findings.append("The environment represents -1 cells in the grid; confirm whether each -1 is a terminal trap or an impassable obstacle.")
        if "is_valid_position" in env_code and "return self.GRID[row][col] != -1" in env_code:
            findings.append("All -1 cells are currently treated as invalid positions, so the robot cannot enter the penalty cell. Check whether this matches the lab's intended trap behavior.")
        if "GOAL" in env_code and "done = True" in env_code:
            findings.append("The environment appears to mark reaching the goal as terminal; verify that the goal is the intended recharge/home state.")

    if not q_code:
        findings.append("No q_learning.py content was provided; learning updates could not be checked.")
    else:
        if "epsilon" in q_code and "random.random()" in q_code:
            findings.append("The agent uses epsilon-greedy exploration.")
        if "updated_q = current_q + self.alpha" in q_code:
            findings.append("The Q update follows the standard incremental Q-learning form.")
        if "best_next_q = max" in q_code:
            findings.append("The update bootstraps from the maximum next-state Q-value for nonterminal transitions.")

    if not main_code:
        findings.append("No main.py content was provided; execution flow could not be checked.")
    else:
        if "episodes=5" in main_code:
            findings.append("The demo trains for only five episodes; this is useful for a smoke test but usually too few to assess learning.")

    if not findings:
        findings.append("No obvious patterns matched the built-in checks. A human review is still needed.")

    return (
        "CODE REVIEW REPORT\n"
        f"Context received: {', '.join(sorted(context.keys()))}\n"
        + "\n".join(f"- {item}" for item in findings)
    )
