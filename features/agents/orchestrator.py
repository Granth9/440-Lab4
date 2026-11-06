import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from features.agents import hyperparam_agent, policy_agent

CONTEXT = Path(__file__).resolve().parent / "context"

ALLOWED = {
    "hyperparam": ["project.md", "hyperparams.md"],
    "policy": ["project.md", "policy.md"],
}


def load_context(agent_name):
    files = {}
    for name in ALLOWED[agent_name]:
        files[name] = (CONTEXT / name).read_text()
    return files


def main():
    print("=== sub-agents demo ===")
    hp_ctx = load_context("hyperparam")
    pol_ctx = load_context("policy")

    print("hyperparam agent gets:", ", ".join(hp_ctx))
    print("policy agent gets:", ", ".join(pol_ctx))
    print("each agent only sees its own context\n")

    print(hyperparam_agent.run(hp_ctx))
    print()
    print(policy_agent.run(pol_ctx))


if __name__ == "__main__":
    main()
