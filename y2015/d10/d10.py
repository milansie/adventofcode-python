from common.advent_day import AdventDay



class D10(AdventDay):


    def first(self, lines: list[str]) -> str:

        counter = 40
        line = lines[0]

        return self.process(line, counter)


    def second(self, lines: list[str]) -> str:

        counter = 50
        line = lines[0]

        return self.process(line, counter)

    @staticmethod
    def process(line: str, counter: int) -> str:

        for _ in range(counter):
            result = []
            prev_char = line[0]
            count_char = 1

            for current_char in line[1:]:

                if current_char == prev_char:
                    count_char += 1
                else:
                    result.append(f"{count_char}{prev_char}")
                    count_char = 1
                    prev_char = current_char

            result.append(f"{count_char}{prev_char}")
            line = ''.join(result)

        return str(len(line))


if __name__ == "__main__":
    day = D10()
    day.run()