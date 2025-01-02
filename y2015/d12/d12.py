import json
import typing

from common.advent_day import AdventDay

class D12(AdventDay):

    def first(self, lines: list[str]) -> str:

        data = json.loads(lines[0])
        result = self.count_numbers(data, False)

        return str(result)


    def second(self, lines: list[str]) -> str:

        data = json.loads(lines[0])
        result = self.count_numbers(data, True)

        return str(result)

    def count_numbers(self, data: typing.Union[list, dict], ignore_red: bool):

        if isinstance(data, (int, float)):
            return data

        if isinstance(data, dict):
            if ignore_red and ("red" in data.values() or "red" in data):
                return 0
            data = data.values()

        return sum(self.count_numbers(item, ignore_red)
                   for item in data
                   if isinstance(item, (int, float, dict, list)))


if __name__ == "__main__":
    day = D12()
    day.run()