from enum import Enum

class Instruction(Enum):
    AND = 0
    OR = 1
    XOR = 2
    NOT = 3
    RSHIFT = 4
    LSHIFT = 5
    SET = 6


    @staticmethod
    def from_str(param: str) -> "Instruction":
        if param in Instruction.__members__:
            return Instruction.__members__[param]
        raise ValueError(f"Invalid instruction: {param}")


class Gate:

    def __init__(self, output: str, instruction: Instruction, input1: str, input2: str | None):
        self.input1 = input1
        self.input2 = input2
        self.output = output
        self.instruction = instruction

    def __str__(self) -> str:
        return f"{self.output} = {self.instruction.name} {self.input1}, {self.input2}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self):
        return hash((self.output, self.input1, self.input2, self.instruction))

    def __eq__(self, other):
        if not isinstance(other, Gate):
            return False
        return self.output == other.output and self.input1 == other.input1 and self.input2 == other.input2 and self.instruction == other.instruction


    def perform_int_action(self, input1: int, input2: int | None) -> int:

        match self.instruction:
            case Instruction.AND:
                return input1 & input2
            case Instruction.OR:
                return input1 | input2
            case Instruction.XOR:
                return input1 ^ input2
            case Instruction.NOT:
                return ~input1 & 0xFFFF
            case Instruction.RSHIFT:
                return input1 >> input2
            case Instruction.LSHIFT:
                return input1 << input2
            case Instruction.SET:
                return input1