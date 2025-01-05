import re

from common.advent_day import AdventDay


class D16(AdventDay):

    sues: dict[int, dict[str, int]] = dict()

    card = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
            'trees': 3, 'cars': 2, 'perfumes': 1}
    
    def __init__(self):
        super().__init__()

    def reinit(self):
        sues = dict()

    def first(self, lines: list[str]) -> str:

        self.parse(lines)
        return self.find(True)

    def second(self, lines: list[str]) -> str:
        self.parse(lines)
        return self.find(False)



    def parse(self, lines: list[str]):
        pattern_line = r"Sue (\d+): (.*)"
        pattern_prop = r"(\w+): (\d+)"

        self.sues = {
            int(match.group(1)): {
                prop: int(value)
                for prop, value in re.findall(pattern_prop, match.group(2))
            }
            for line in lines
            if (match := re.match(pattern_line, line))
        }


    def find(self, first: bool):

        possible_sues = set(self.sues.keys())

        for prop, value in self.card.items():
            sues_to_remove = set()
            for sue in possible_sues:

                if first:
                    if self.sues[sue].get(prop) is not None and self.sues[sue].get(prop) != value:
                        sues_to_remove.add(sue)
                else:
                    if self.sues[sue].get(prop) is not None:
                        if prop in ['cats', 'trees']:
                            if self.sues[sue].get(prop) <= value:
                                sues_to_remove.add(sue)
                        elif prop in ['pomeranians', 'goldfish']:
                            if self.sues[sue].get(prop) >= value:
                                sues_to_remove.add(sue)
                        else:
                            if self.sues[sue].get(prop) != value:
                                sues_to_remove.add(sue)

            possible_sues -= sues_to_remove
        print("\n".join(f"{sue}: {self.sues[sue]}" for sue in possible_sues))

        return str(next(iter(possible_sues)))


if __name__ == "__main__":
    day = D16()
    day.run()