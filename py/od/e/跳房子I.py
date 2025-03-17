class Point:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __str__(self):
        return f"[{self.a}, {self.b}]"


d = {}

nums = list(map(int, input()[1:-1].split(",")))
target = int(input())

res = None


for i, num in enumerate(nums):
    if (target - num) in d:
        p = Point(target - num, num, d[target - num] + i)
        if res:
            res = min(res, p)
        else:
            res = p
    if num not in d:
        d[num] = i

print(res)
