from enum import Enum

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    EAST = RIGHT
    WEST = LEFT
    NORTH = UP
    SOUTH = DOWN

    @classmethod
    def from_char(cls, direction_str: str) -> "Direction | None":
        return {
            '^': cls.UP,
            'v': cls.DOWN,
            '<': cls.LEFT,
            '>': cls.RIGHT
        }.get(direction_str)

    def to_char(self) -> str:
        return {
            Direction.UP: "^",
            Direction.DOWN: "v",
            Direction.LEFT: "<'",
            Direction.RIGHT: ">"
        }[self]

    def left(self) -> "Direction":
        """Return the direction after rotating 90 degrees left."""
        return {
            Direction.UP: Direction.LEFT,
            Direction.DOWN: Direction.RIGHT,
            Direction.LEFT: Direction.DOWN,
            Direction.RIGHT: Direction.UP
        }[self]

    def right(self) -> "Direction":
        """Return the direction after rotating 90 degrees right."""
        return {
            Direction.UP: Direction.RIGHT,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.RIGHT: Direction.DOWN
        }[self]

    @classmethod
    def cardinals(cls) -> list[tuple[int, int]]:
        return [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

    @classmethod
    def all_direction(cls) -> list[tuple[int, int]]:
        return [
            (0, -1),  # up
            (0, 1),   # down
            (-1, 0),  # left
            (1, 0),   # right
            (-1, -1), # up left
            (1, -1),  # up right
            (-1, 1),  # down left
            (1, 1)    # down right
        ]
