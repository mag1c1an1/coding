n = int(input())


def solve(days):
    abc = 0
    l = 0
    prev = None
    cnt = 0
    for r, val in enumerate(days):
        if val == "absent":
            abc += 1
            cnt += 1
            if abc >= 2:
                return False

        if val in ["late", "leaveearly"]:
            cnt += 1
            if prev and prev in ["late", "leaveearly"]:
                return False
        prev = val
        if r - l + 1 == 7:
            if cnt >= 3:
                return False
            if days[l] != "present":
                cnt -= 1
            l += 1
    return True


res = []
for _ in range(n):
    days = list(input().split())
    res.append(solve(days))

print(" ".join(["true" if v else "false" for v in res]))
