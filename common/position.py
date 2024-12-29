from dataclasses import dataclass

from common.direction import Direction


@dataclass
class Position:
    x: int
    y: int
    
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    @classmethod
    def from_position(cls, other: "Position") -> "Position":
        return cls(other.x, other.y)


    def change(self, direction: "Direction"):

        changes = {
            Direction.UP: (0, 1),
            Direction.DOWN: (0, -1),
            Direction.LEFT: (-1, 0),
            Direction.RIGHT: (1, 0)
        }

        dx, dy = changes[direction]
        self.x += dx
        self.y += dy
