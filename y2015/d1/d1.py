from common.advent_day import AdventDay


class D1(AdventDay):

    def first(self, lines: list[str]) -> str:
        result = ""

        for line in lines:
            floor = 0

            for char in line:
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1

            result += str(floor)

        return result

    def second(self, lines: list[str]) -> str:

        result = ""

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
                    result += str(count)
                    break

        return result


if __name__ == "__main__":
    d1 = D1()
    d1.run()