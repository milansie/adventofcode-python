import random

from common.advent_day import AdventDay

class D19(AdventDay):

    molecule = dict()

    def __init__(self):
        super().__init__()
        
    def reinit(self):
        self.molecule = dict()

    def first(self, lines: list[str]) -> str:
        
        input = self.parse(lines)
        return self.process_first(input)


    def second(self, lines: list[str]) -> str:
        input = self.parse(lines)
        return self.process_second(input)

    def parse(self, lines) -> str:
        
        for line in lines:
            if line.count(" => ") == 1:
                input, output = line.split(" => ")
                self.molecule.setdefault(input, []).append(output)
                continue
                
            if line != "":
                return line

    def process_first(self, input):

        new_molecules = set()

        for i in range(len(input)):

            repl = input[i]

            if i < len(input) - 1:
                if input[i:i+2] in self.molecule:
                    repl = input[i:i+2]

            if repl in self.molecule:

                for new_repl in self.molecule[repl]:
                    new_input = input[:i] + new_repl + input[i+len(repl):]
                    new_molecules.add(new_input)

            if len(repl)> 1:
                i = i + 1

        return str(len(new_molecules))


    def process_second(self, input) -> str:

        rules_list = [(out, inp) for inp, outs in self.molecule.items() for out in outs]

        for attempt in range(1000):
            random.shuffle(rules_list)
            steps = 0
            current_molecule = input

            while current_molecule != "e":
                replaced = False
                for out, inp in rules_list:
                    if out in current_molecule:
                        current_molecule = current_molecule.replace(out, inp, 1)
                        steps += 1
                        replaced = True
                        break
                if not replaced:
                    break
            else:
                return str(steps)

        return str(-1)




if __name__ == "__main__":
    day = D19()
    day.run()