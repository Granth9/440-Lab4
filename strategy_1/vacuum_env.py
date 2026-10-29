from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

Position = Tuple[int, int]
Action = str


@dataclass(frozen=True)
class Transition:
    next_state: Position
    reward: float
    done: bool
    info: Dict[str, object]


class VacuumEnvironment:
    GRID = [
        [0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, -1, 0, 10],
    ]

    START = (0, 0)
    GOAL = (3, 3)
    PENALTY = (3, 1)
    ACTIONS: List[Action] = ["up", "down", "left", "right"]

    def __init__(self) -> None:
        self.current_pos = self.START
        self.done = False

    def reset(self) -> Position:
        self.current_pos = self.START
        self.done = False
        return self.current_pos

    def is_valid_position(self, pos: Position) -> bool:
        row, col = pos
        if row < 0 or row >= len(self.GRID) or col < 0 or col >= len(self.GRID[0]):
            return False
        return self.GRID[row][col] != -1

    def step(self, action: Action) -> Transition:
        if self.done:
            raise ValueError("The environment is finished. Call reset() first.")

        row, col = self.current_pos
        if action == "up":
            next_pos = (row - 1, col)
        elif action == "down":
            next_pos = (row + 1, col)
        elif action == "left":
            next_pos = (row, col - 1)
        elif action == "right":
            next_pos = (row, col + 1)
        else:
            raise ValueError(f"Unknown action: {action}")

        if not self.is_valid_position(next_pos):
            next_pos = self.current_pos
            reward = -1.0
            done = False
        elif next_pos == self.GOAL:
            reward = 10.0
            done = True
        elif next_pos == self.PENALTY:
            reward = -1.0
            done = True
        else:
            reward = 0.0
            done = False

        self.current_pos = next_pos
        self.done = done

        return Transition(
            next_state=self.current_pos,
            reward=reward,
            done=done,
            info={"position": self.current_pos, "action": action},
        )

    def render(self) -> str:
        rows: List[str] = []
        for r, row in enumerate(self.GRID):
            cells: List[str] = []
            for c, value in enumerate(row):
                if (r, c) == self.current_pos:
                    cells.append("R")
                elif (r, c) == self.GOAL:
                    cells.append("G")
                elif (r, c) == self.PENALTY:
                    cells.append("P")
                elif value == -1:
                    cells.append("X")
                else:
                    cells.append("0")
            rows.append(" ".join(cells))
        return "\n".join(rows)
