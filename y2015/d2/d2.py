from common.advent_day import AdventDay


class D2(AdventDay):

    def first(self, lines: list[str]) -> str:
        result = 0

        for line in lines:
            l, w, h = map(int, line.split("x"))

            wh = w * h
            wl = w * l
            hl = h * l

            result += 2*wh + 2*wl + 2*hl + min(wh, wl, hl)

        return str(result)

    def second(self, lines: list[str]) -> str:

        result = 0

        for line in lines:
            l, w, h = map(int, line.split("x"))

            dimensions = sorted([l, w, h])
            first, second = dimensions[:2]

            ribbon = 2 * first + 2 * second
            bow = l * w * h

            result += ribbon + bow
            
        return str(result)


if __name__ == "__main__":
    day = D2()
    day.run()