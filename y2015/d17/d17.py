from common.advent_day import AdventDay


class D17(AdventDay):

    TEST_TARGET = 25
    PROD_TARGET = 150

    def __init__(self):
        super().__init__()

    def first(self, lines: list[str]) -> str:

        target = self.TEST_TARGET if self.IN_TEST else self.PROD_TARGET

        containers = list(map(int, lines))

        combinations = [0] * (target + 1)
        combinations[0] = 1

        for container in containers:

            for i in range(target, container - 1, -1):
                combinations[i] += combinations[i - container]


        return str(combinations[target])

    def second(self, lines: list[str]) -> str:
        target = self.TEST_TARGET if self.IN_TEST else self.PROD_TARGET

        containers = list(map(int, lines))
        min_containers = [float('inf')] * (target + 1)
        min_containers[0] = 0

        min_combinations = [0] * (target + 1)
        min_combinations[0] = 1

        combinations = [0] * (target + 1)
        combinations[0] = 1

        for container in containers:

            for i in range(target, container - 1, -1):
                if combinations[i - container] > 0:

                    combinations[i] += combinations[i - container]

                    if min_containers[i] > min_containers[i - container] + 1:
                        min_containers[i] = min_containers[i - container] + 1
                        min_combinations[i] = min_combinations[i - container]
                    elif min_containers[i] == min_containers[i - container] + 1:
                        min_combinations[i] += min_combinations[i - container]


        return str(min_combinations[target])

if __name__ == "__main__":
    day = D17()
    day.run()