NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)
ACTIONS = [NORTH, SOUTH, EAST, WEST]

ARROWS = {NORTH: "^", SOUTH: "v", EAST: ">", WEST: "<", None: "."}


def turn_right(a):
    return {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}[a]


def turn_left(a):
    return {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}[a]


class GridMDP:
    def __init__(self, living_reward=-0.04, discount=0.9):
        grid = [
            [living_reward, living_reward, living_reward, 1.0],
            [living_reward, None, living_reward, -1.0],
            [living_reward, living_reward, living_reward, living_reward],
        ]
        grid = list(reversed(grid))

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.gamma = discount
        self.init = (0, 0)
        self.terminals = {(3, 2), (3, 1)}
        self.actions_list = ACTIONS[:]

        self.reward = {}
        self.states = set()
        for x in range(self.cols):
            for y in range(self.rows):
                if grid[y][x] is not None:
                    self.states.add((x, y))
                    self.reward[(x, y)] = grid[y][x]

        self.transitions = {}
        for s in self.states:
            self.transitions[s] = {}
            for a in self.actions_list:
                self.transitions[s][a] = [
                    (0.8, self.go(s, a)),
                    (0.1, self.go(s, turn_right(a))),
                    (0.1, self.go(s, turn_left(a))),
                ]

    def R(self, s):
        return self.reward[s]

    def T(self, s, a):
        if a is None:
            return [(0.0, s)]
        return self.transitions[s][a]

    def actions(self, s):
        if s in self.terminals:
            return [None]
        return self.actions_list[:]

    def go(self, s, direction):
        nxt = (s[0] + direction[0], s[1] + direction[1])
        if nxt in self.states:
            return nxt
        return s

    def policy_arrows(self, policy):
        lines = []
        for y in reversed(range(self.rows)):
            row = []
            for x in range(self.cols):
                s = (x, y)
                if s not in self.states:
                    row.append("#")
                else:
                    row.append(ARROWS.get(policy.get(s), "?"))
            lines.append(" ".join(row))
        return "\n".join(lines)
