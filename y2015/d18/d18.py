from common.advent_day import AdventDay
from common.utils import init_map
from common.utils import render_map

import numpy as np

class D18(AdventDay):


    def __init__(self):
        super().__init__()

    def first(self, lines: list[str]) -> str:

        size = 6 if self.IN_TEST else 100
        steps = 4 if self.IN_TEST else 100

        lights_map = init_map(size, size)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                lights_map[y][x] = char == "#"

        lights_map = self.process_map(lights_map, size, steps, set())

        return str(np.sum(lights_map))

    def second(self, lines: list[str]) -> str:

        size = 6 if self.IN_TEST else 100
        steps = 5 if self.IN_TEST else 100

        lights_map = init_map(size, size)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                lights_map[y][x] = char == "#"

        fixed = {(0, 0), (0, size - 1), (size -1, 0), (size -1, size -1)}
        for y, x in fixed:
            lights_map[y][x] = True

        lights_map = self.process_map(lights_map, size, steps, fixed)

        return str(np.sum(lights_map))

    @staticmethod
    def process_map(lights_map: np.ndarray, size: int, steps: int, fixed: set[tuple[int, int]]) -> np.ndarray:
        for _ in range(steps):

            padded = np.pad(lights_map, 1, mode='constant', constant_values=0)
            neighbours = np.zeros((size, size), dtype=int)

            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue
                    neighbours += padded[i:i+size, j:j+size]

            new_map = (lights_map & ((neighbours == 2) | (neighbours == 3))) | \
                      (np.logical_not(lights_map) & (neighbours == 3))

            if fixed:
                for y, x in fixed:
                    new_map[y, x] = True

            lights_map = new_map

        return lights_map


if __name__ == "__main__":
    day = D18()
    day.run()