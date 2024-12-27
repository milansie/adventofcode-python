from common.advent_day import AdventDay


class D1(AdventDay):
    def __init__(self):
        super().__init__()


    def first(self, lines: list[str]) -> str:
        result = ""

        for line in lines:
            floor = 0

            for char in line:
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1

            result += f"{floor}"

        return result

    def second(self, lines: list[str]) -> str:

        for line in lines:
            floor = 0
            count = 0
            for char in line:
                count += 1
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1

                if floor < 0:
                    return f"{count}"

        return "-1"


if __name__ == "__main__":
    d1 = D1()
    d1.run()