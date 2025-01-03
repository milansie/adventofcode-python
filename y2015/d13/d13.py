import re
from collections import deque

from common.advent_day import AdventDay

class ArrangementStep:
    def __init__(self, attendee: str, arrangement):
        self.attendee = attendee
        self.arrangement = arrangement
        self.visited = [attendee]

    def __repr__(self):
        return f"{self.attendee} {self.arrangement} {self.visited}"

class D13(AdventDay):
    
    def __init__(self):
        super().__init__()
        self.attendees_relations = dict()
        self.attendees = set()


    def first(self, lines: list[str]) -> str:
        self.parse(lines)

        return str(self.find_best_arrangement())


    def second(self, lines: list[str]) -> str:
        self.parse(lines)

        for attendee in self.attendees:
            self.attendees_relations[(attendee, "me")] = 0
            self.attendees_relations[("me", attendee)] = 0

        self.attendees.add("me")

        return str(self.find_best_arrangement())


    def parse(self, lines: list[str]):

        for line in lines:
            match = re.match(r'(\w+) would (\w+) (\d+) happiness.*to (\w+).', line)
            points = int(match.group(3))
            if match.group(2) == "lose":
                points *= -1

            self.attendees_relations[(match.group(1), match.group(4))] = points
            self.attendees.add(match.group(1))
            self.attendees.add(match.group(4))

    def find_best_arrangement(self):

        best_arrangement = 0 - float('inf')
        best_way = None

        queue = deque()
        queue.extend(ArrangementStep(attendee, 0) for attendee in self.attendees)

        while queue:
            current = queue.popleft()

            if len (current.visited) == len(self.attendees):

                possible_arrangement = (current.arrangement +
                                        self.attendees_relations[(current.visited[0], current.visited[-1])] +
                                        self.attendees_relations[(current.visited[-1], current.visited[0])])

                if possible_arrangement > best_arrangement:
                    best_arrangement = possible_arrangement
                    best_way = current
                    continue

            for attendee in self.attendees:
                if attendee not in current.visited:
                    new_arrangement = (current.arrangement +
                                       self.attendees_relations[(current.attendee, attendee)] +
                                       self.attendees_relations[(attendee, current.attendee)]
                                       )

                    new_step = ArrangementStep(attendee, new_arrangement)
                    new_step.visited = current.visited[:]
                    new_step.visited.append(attendee)
                    queue.append(new_step)


        return best_arrangement


if __name__ == "__main__":
    day = D13()
    day.run()