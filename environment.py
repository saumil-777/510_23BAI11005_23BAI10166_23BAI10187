import numpy as np

class GridWorld:
    def __init__(self, size=6):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)  # better

        # obstacles
        self.grid[1][2] = 1
        self.grid[2][2] = 1
        self.grid[3][3] = 1
        self.grid[4][1] = 1
        self.grid[2][4] = 1

        self.start = (0, 0)
        self.goal = (size-1, size-1)

    def is_valid(self, state):
        x, y = state
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] == 0

    def get_actions(self):
        return [(0,1),(1,0),(0,-1),(-1,0)]