class Cap:
    def __init__(self, s):
        self.s = s

    def parse(self) -> int:
        val = 0
        unit = ""
        total = 0
        for i, c in enumerate(self.s):
            if c.isdigit():
                val = val * 10 + int(c)
            else:
                unit += c
                val = self.exchange(val, unit)
                total += val
                val = 0
                unit = ""
        return total

    def exchange(self, val, unit):
        match unit:
            case "M":
                return val
            case "G":
                return 1024 * val
            case "T":
                return 1024 * 1024 * val

    def __lt__(self, other):
        return self.parse() < other.parse()

    def __str__(self):
        return self.s


def main():
    n = int(input())
    cs = []
    for _ in range(n):
        cs.append(Cap(input()))
    cs.sort()
    for cap in cs:
        print(cap)


if __name__ == "__main__":
    main()
