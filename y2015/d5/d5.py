import re

from common.advent_day import AdventDay


class D5(AdventDay):

    def first(self, lines: list[str]) -> str:
        return str(sum (1 for line in lines if all ([
            self.contain_vowels(line),
            self.contain_double_letter(line),
            self.not_contain_forbidden(line)])))


    def second(self, lines: list[str]) -> str:
        return str(sum (1 for line in lines if all ([
            self.contain_double_letter_with_other_between(line),
            self.contain_two_letters_twice(line)])))

    @staticmethod
    def contain_vowels(line: str) -> bool:
        return len(re.findall(r'[aeiou]', line)) >= 3

    @staticmethod
    def contain_double_letter(line: str) -> bool:
        return bool(re.search(r'.*([a-z])\1.*', line))

    @staticmethod
    def not_contain_forbidden(line: str) -> bool:
        return not bool(re.search(r'(ab|cd|pq|xy)', line))

    @staticmethod
    def contain_double_letter_with_other_between(line: str) -> bool:
        return bool(re.search(r'.*([a-z]).\1.*', line))

    @staticmethod
    def contain_two_letters_twice(line: str) -> bool:
        return bool(re.search(r'.*([a-z][a-z]).*\1.*', line))

if __name__ == "__main__":
    day = D5()
    day.run()