from collections import deque

from common.advent_day import AdventDay
from common.gate import Gate
from common.gate import Instruction


class D7(AdventDay):

    def __init__(self):
        super().__init__()
        self.gates = {}
        self.wiremap = {}

    def first(self, lines: list[str]) -> str:

        self.parse(lines)
        self.execute()

        if self.IN_TEST:
            return "\n".join(f"{key}: {value}" for key, value in sorted(self.wiremap.items()))
        else:
            return str(self.wiremap["a"])


    def second(self, lines: list[str]) -> str:
        self.parse(lines)
        self.execute()

        if self.IN_TEST:
            return "\n".join(f"{key}: {value}" for key, value in sorted(self.wiremap.items()))
        else:
            a = str(self.wiremap["a"])

            self.wiremap = {}
            self.gates = {}

            self.parse(lines)
            self.gates["b"].input1 = a

            self.execute()
            return str(self.wiremap["a"])


    def parse(self, lines: list[str]):
        for line in lines:
            parts = line.split(" ")

            match line.split():
                case [value, "->", output]:
                    # SET ie. "123 -> x"
                    self.gates[output] = Gate(output, Instruction.SET, value, None)

                case ["NOT", input1, "->", output]:
                    # NOT : ie "NOT x -> h"
                    self.gates[output] = Gate(output, Instruction.NOT, input1, None)

                case [input1, op, input2, "->", output]:
                    # binary operation: ie. "x AND y -> d"
                    self.gates[output] = Gate(output, Instruction.from_str(op), input1, input2)

    def execute(self):

        in_degree = {key: 0 for key in self.wiremap}
        depend_on_me = {key: [] for key in self.wiremap}

        for gate in self.gates.values():

            if gate.instruction == Instruction.SET and gate.input1.isdigit():
                self.wiremap[gate.output] = int(gate.input1)
                in_degree[gate.output] = 0
                continue

            if gate.input1 in self.gates:
                in_degree[gate.output] = in_degree.get(gate.output, 0) + 1

            depend_on_me.setdefault(gate.input1, []).append(gate.output)

            if gate.input2 and gate.input2 in self.gates:
                in_degree[gate.output] = in_degree.get(gate.output, 0) + 1

            if gate.input2:
                depend_on_me.setdefault(gate.input2, []).append(gate.output)

        queue = deque()

        queue.extend(key for key in in_degree if in_degree[key] == 0)

        while queue:
            key = queue.popleft()
            gate = self.gates[key]

            if gate:
                input1 = int(gate.input1) if gate.input1.isdigit() else self.wiremap.get(gate.input1)
                input2 = int(gate.input2) if gate.input2 and gate.input2.isdigit() else self.wiremap.get(gate.input2) if gate.input2 else None

                self.wiremap[gate.output] = gate.perform_int_action(input1, input2)

            if key in depend_on_me:
                for depending in depend_on_me[key]:
                    if depending not in in_degree:
                        queue.append(depending)
                    else:
                        in_degree[depending] -= 1
                        if in_degree[depending] == 0:
                            queue.append(depending)



if __name__ == "__main__":
    day = D7()
    day.run()