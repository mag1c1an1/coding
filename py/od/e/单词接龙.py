from collections import defaultdict, deque
from functools import cmp_to_key


def cmp(a, b):
    if len(a) > len(b):
        return -1
    elif len(a) < len(b):
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0


def main():
    k = int(input())
    n = int(input())
    d = defaultdict(deque)
    start = ""
    for i in range(n):
        s = input()
        if i == k:
            start = s
            continue
        d[s[0]].append(s)

    for k, v in d.items():
        d[k] = deque(sorted(v, key=lambda x: (-len(x), x)))

    ans = start

    def dfs(curr):
        nonlocal ans
        if len(curr) > len(ans):
            ans = curr

        if len(d[curr[-1]]) == 0:
            return
        v = d[curr[-1]].popleft()

        dfs(curr + v)

    # vis[start] = True
    dfs(start)
    print(ans)


if __name__ == "__main__":
    main()
