import re

from common.advent_day import AdventDay

class D14(AdventDay):
    
    def __init__(self):
        super().__init__()
        self.reindeers: dict[str, tuple[int, int, int]] = dict()



    def first(self, lines: list[str]) -> str:
        self.reindeers: dict[str, tuple[int, int, int]] = dict()

        self.parse(lines)

        seconds = 1000 if self.IN_TEST else 2503
        max_distance = 0
        for reindeer in self.reindeers:
            distance = self.get_distance(self.reindeers[reindeer], seconds)
            if distance > max_distance:
                max_distance = distance


        return str(max_distance)


    def second(self, lines: list[str]) -> str:
        self.reindeers = dict()

        self.parse(lines)

        seconds = 1000 if self.IN_TEST else 2503

        race = {reindeer: 0 for reindeer in self.reindeers}

        for second in range(1, seconds + 1):
            max_distance = 0
            max_reindeer = list()
            for reindeer in self.reindeers:
                distance = self.get_distance(self.reindeers[reindeer], second)
                if distance > max_distance:
                    max_distance = distance
                    max_reindeer = [reindeer]
                elif distance == max_distance:
                    max_reindeer.append(reindeer)

            for reindeer in max_reindeer:
                race[reindeer] += 1


        return str(max(race.values()))


    def parse(self, lines: list[str]):
        pattern = r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<fly_time>\d+) seconds.*for (?P<rest_time>\d+) seconds.'

        for line in lines:
            match = re.match(pattern, line)
            self.reindeers[match.group('name')] = (
                int(match.group('speed')),
                int(match.group('fly_time')),
                int(match.group('rest_time'))
            )

    @staticmethod
    def get_distance(reindeer_data: tuple[int, int, int], seconds: int) -> int:
        speed, fly_time, rest_time = reindeer_data

        interval = fly_time + rest_time
        count = seconds // interval
        last_distance = min(seconds % interval, fly_time) * speed

        return count * fly_time * speed + last_distance

if __name__ == "__main__":
    day = D14()
    day.run()