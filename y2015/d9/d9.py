from collections import deque

from common.advent_day import AdventDay

class LocationStep:
    def __init__(self, city, distance):
        self.city = city
        self.distance = distance
        self.visited = [city]

    def __repr__(self):
        return f"{self.city} {self.distance} {self.visited}"


class D9(AdventDay):

    def __init__(self):
        self.distances = {}
        self.cities = set()

        super().__init__()


    def first(self, lines: list[str]) -> str:
        self.distances = {}
        self.cities = set()

        self.parse(lines)

        return str(self.find_way(True))

    def second(self, lines: list[str]) -> str:
        self.distances = {}
        self.cities = set()

        self.parse(lines)

        return str(self.find_way(False))

    def parse(self, lines):
        for line in lines:
            match line.split():
                case [city1, "to", city2, "=", distance]:
                    self.distances[(city1, city2)] = int(distance)
                    self.distances[(city2, city1)] = int(distance)
                    self.cities.add(city1)
                    self.cities.add(city2)

    def find_way(self, shortest: bool) -> int:

        best_distance = float('inf') if shortest else 0
        best_way = None

        queue = deque()
        queue.extend(LocationStep(city, 0) for city in self.cities)

        while queue:
            current = queue.popleft()

            if shortest and current.distance > best_distance:
                continue

            if len (current.visited) == len(self.cities):
                if shortest and current.distance < best_distance:
                    best_distance = current.distance
                    best_way = current
                    continue
                
                if not shortest and current.distance > best_distance:
                    best_distance = current.distance
                    best_way = current
                    continue

            for city in self.cities:
                if city not in current.visited:
                    new_distance = current.distance + self.distances[(current.city, city)]
                    new_step = LocationStep(city, new_distance)
                    new_step.visited = current.visited[:]
                    new_step.visited.append(city)
                    queue.append(new_step)

        return best_way.distance


if __name__ == "__main__":
    day = D9()
    day.run()