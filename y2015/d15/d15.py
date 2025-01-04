import re
from dataclasses import dataclass

from common.advent_day import AdventDay

@dataclass
class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __repr__(self):
        return f"{self.name} C:{self.capacity} D:{self.durability} F:{self.flavor} T:{self.texture} Ca:{self.calories}"

class D15(AdventDay):

    ingredients: list[Ingredient] = list()
    
    def __init__(self):
        super().__init__()

    def reinit(self):
        self.ingredients = list()


    def first(self, lines: list[str]) -> str:

        self.parse(lines)

        if self.IN_TEST:
            return str(max(
                self.compute_test_ingredients(i, False) for i in range(100)
            ))
        else:
            return str(max(
                self.compute_ingredients(i, j, k, False) for i in range(100) for j in range(100) for k in range(100)
            ))


    def second(self, lines: list[str]) -> str:
        self.parse(lines)

        if self.IN_TEST:
            return str(max(
                self.compute_test_ingredients(i, True) for i in range(100)
            ))
        else:
            return str(max(
                self.compute_ingredients(i, j, k, True) for i in range(100) for j in range(100) for k in range(100)
            ))


    def parse(self, lines: list[str]):
        pattern = r'(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)'

        for line in lines:
            match = re.match(pattern, line)
            self.ingredients.append(Ingredient(match.group('name'), int(match.group('capacity')), int(match.group('durability')), int(match.group('flavor')), int(match.group('texture')), int(match.group('calories'))))

    def compute_test_ingredients(self, first: int, check_calories: bool) -> int:
        second = 100 - first
        capacity = self.ingredients[0].capacity * first + self.ingredients[1].capacity * second
        durability = self.ingredients[0].durability * first + self.ingredients[1].durability * second
        flavor = self.ingredients[0].flavor * first + self.ingredients[1].flavor * second
        texture = self.ingredients[0].texture * first + self.ingredients[1].texture * second

        if check_calories and self.ingredients[0].calories * first + self.ingredients[1].calories * second != 500:
            return 0

        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
            return 0

        return capacity * durability * flavor * texture

    def compute_ingredients(self, first: int, second: int, third: int, check_calories: bool) -> int:
        fourth = 100 - first - second - third

        capacity = self.ingredients[0].capacity * first + self.ingredients[1].capacity * second + self.ingredients[2].capacity * third + self.ingredients[3].capacity * fourth
        durability = self.ingredients[0].durability * first + self.ingredients[1].durability * second + self.ingredients[2].durability * third + self.ingredients[3].durability * fourth
        flavor = self.ingredients[0].flavor * first + self.ingredients[1].flavor * second + self.ingredients[2].flavor * third + self.ingredients[3].flavor * fourth
        texture = self.ingredients[0].texture * first + self.ingredients[1].texture * second + self.ingredients[2].texture * third + self.ingredients[3].texture * fourth

        if check_calories and self.ingredients[0].calories * first + self.ingredients[1].calories * second + self.ingredients[2].calories * third + self.ingredients[3].calories * fourth != 500:
            return 0

        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
            return 0

        return capacity * durability * flavor * texture


if __name__ == "__main__":
    day = D15()
    day.run()