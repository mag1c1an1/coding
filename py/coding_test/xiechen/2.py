t = int(input())


def solve(a, p, b, n, m):
    arr = []
    for i in range(n):
        arr.append((a[i], p[i]))

    arr.sort(key=lambda v: v[0])
    ans = 0
    for i, v in enumerate(b):
        tmp  = 0
        for j in range(n):
            if arr[j][0] <= v:
                tmp = max(tmp, arr[j][1])
        ans += tmp

    print(ans)


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(a, p, b, n, m)
