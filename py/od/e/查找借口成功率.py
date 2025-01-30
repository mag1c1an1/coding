def main():
    avg = int(input())
    arr = list(map(int, input().split()))
    l = 0
    s = 0
    n = 0
    ans = []
    res = 0
    for r, v in enumerate(arr):
        n += 1
        s += v
        while n > 0 and s / n > avg:
            s -= arr[l]
            n -= 1
            l += 1
        if r - l + 1 > res:
            res = r - l + 1
            ans = [(l, r)]
        elif r - l + 1 == res:
            ans.append((l, r))

    out = []
    for p in ans:
        out.append(f"{p[0]}-{p[1]}")
    print(" ".join(out) if len(out) > 0 else "NULL")


if __name__ == "__main__":
    main()
