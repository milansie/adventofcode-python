from hashlib import md5
from common.advent_day import AdventDay


class D4(AdventDay):

    def first(self, lines: list[str]) -> str:
        return ",".join(self.count_md5(line, 5) for line in lines)


    def second(self, lines: list[str]) -> str:
        return ",".join(self.count_md5(line, 6) for line in lines)

    @staticmethod
    def count_md5(key, zeroes_count) -> str:

        zeroes = "0" * zeroes_count

        number = 0
        while True:
            to_hash = key + str(number)
            md5_hash = md5(to_hash.encode()).hexdigest()
            if md5_hash[:zeroes_count] == zeroes:
                return str(number)
            number += 1


if __name__ == "__main__":
    day = D4()
    day.run()