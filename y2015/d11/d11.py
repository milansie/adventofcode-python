import time

from common.advent_day import AdventDay

class D11(AdventDay):

    def first(self, lines: list[str]) -> str:

        pwd = lines[0]

        while True:
            pwd = self.next_pwd(pwd)

            if self.valid(pwd):
                break

        return pwd


    def second(self, lines: list[str]) -> str:

        pwd = lines[0]

        first = False

        while True:
            pwd = self.next_pwd(pwd)

            if self.valid(pwd):
                if not first:
                    first = True
                    continue
                else:
                    break

        return pwd

    def next_pwd(self, pwd: str) -> str:

        last_char = pwd[-1]
        if last_char == "z":
            return self.next_pwd(pwd[:-1]) + "a"

        return pwd[:-1] + chr(ord(last_char) + 1)


    def next_pwd_2(self, pwd: str) -> str:
        i = len(pwd) - 1

        while i >= 0:
            current_char = pwd[i]
            if current_char == 'z':
                pwd = pwd[:i] + 'a' + pwd[i+1:]
                i -= 1
            else:
                pwd = pwd[:i] +  chr(ord(current_char) + 1) + pwd[i+1:]
                break

        return pwd

    @staticmethod
    def valid(pwd: str) -> bool:

        first_pair = ""
        second_pair = ""
        straight = False

        if ('i' in pwd) or ('o' in pwd) or ('l' in pwd):
            return False

        for i in range(len(pwd)):
            current_char = pwd[i]

            # if current_char in forbidden_chars:
            #     return False

            if i >= 1 and current_char == pwd[i - 1]:
                if first_pair and first_pair != pwd[i - 1] + current_char:
                    second_pair = pwd[i - 1] + current_char
                if not first_pair:
                    first_pair = pwd[i - 1] + current_char

            if i >= 2 and not straight:
                cur2 = pwd[i - 2]
                cur1 = pwd[i - 1]

                if cur1 == chr(ord(cur2) + 1) and current_char == chr(ord(cur1) + 1):
                    straight = True

            if straight and first_pair and second_pair:
                return True

        return False



if __name__ == "__main__":
    day = D11()
    day.run()