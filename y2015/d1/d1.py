from common.advent_day import AdventDay


class D1(AdventDay):
    def __init__(self):
        super().__init__()


    def first(self, lines: list[str]) -> str:
        print("first ")
        return ""

    def second(self, lines: list[str]) -> str:
        print("second ")
        return ""


if __name__ == "__main__":
    d1 = D1()
    result = d1.run()
    print(result)