from common.advent_day import AdventDay
from common.position import Position
from common.direction import Direction


class D3(AdventDay):

    def first(self, lines: list[str]) -> str:
        result = 0

        for line in lines:
            visited_houses = set()
            self._visit_houses(line, visited_houses)
            result += len(visited_houses)

        return str(result)

    def second(self, lines: list[str]) -> str:

        result = 0

        for line in lines:
            visited_houses = set()
            self._visit_houses(line[::2], visited_houses)
            self._visit_houses(line[1::2], visited_houses)
            result += len(visited_houses)

        return str(result)

    @staticmethod
    def _visit_houses(line: str, visited_houses: set[Position]):

        current_position = Position()
        visited_houses.add(current_position)

        line = line.strip()

        for char in line:
            direction = Direction.from_char(char)
            current_position = Position.from_position(current_position)
            current_position.change(direction)
            visited_houses.add(current_position)

if __name__ == "__main__":
    day = D3()
    day.run()