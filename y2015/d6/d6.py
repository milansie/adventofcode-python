import numpy as np
import re

from common.advent_day import AdventDay


class D6(AdventDay):

    def first(self, lines: list[str]) -> str:
        boolean_matrix = np.zeros((1000, 1000), dtype=bool)

        for line in lines:
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))

            if line.startswith("turn on"):
                boolean_matrix[x1:x2+1, y1:y2+1] = True
            elif line.startswith("turn off"):
                boolean_matrix[x1:x2+1, y1:y2+1] = False
            elif line.startswith("toggle"):
                boolean_matrix[x1:x2+1, y1:y2+1] ^= True  # XOR operace pro toggle


        return str(np.sum(boolean_matrix))


    def second(self, lines: list[str]) -> str:
        int_matrix = np.zeros((1000, 1000), dtype=int)

        for line in lines:
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))

            if line.startswith("turn on"):
                int_matrix[x1:x2+1, y1:y2+1] = int_matrix[x1:x2+1, y1:y2+1] + 1
            elif line.startswith("turn off"):
                int_matrix[x1:x2+1, y1:y2+1] = np.maximum(int_matrix[x1:x2+1, y1:y2+1] - 1, 0)
            elif line.startswith("toggle"):
                int_matrix[x1:x2+1, y1:y2+1] = int_matrix[x1:x2+1, y1:y2+1] + 2

        return str(np.sum(int_matrix))

if __name__ == "__main__":
    day = D6()
    day.run()