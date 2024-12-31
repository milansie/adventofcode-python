from common.advent_day import AdventDay
import re

def hex_to_char(match: re.Match) -> str:
    hex_value = match.group(1)
    return chr(int(hex_value, 16))


def convert1(line: str) -> str:

    line = line.replace('\\"', '"').replace('\\\\', '\\')
    pattern = re.compile(r'\\x([0-9a-fA-F]{2})')
    line = re.sub(pattern, hex_to_char, line)

    return line[1:-1]


def convert2(line: str) -> str:

    line = line.replace("\\", "\\\\").replace('"', '\\"')

    return '"' + line + '"'


class D8(AdventDay):

    def first(self, lines: list[str]) -> str:
        return str(sum (len(line) - len(convert1(line)) for line in lines))

    def second(self, lines: list[str]) -> str:
        return str(sum (len(convert2(line)) - len(line) for line in lines))


if __name__ == "__main__":
    day = D8()
    day.run()