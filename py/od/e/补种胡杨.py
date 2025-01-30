def main():
    n = int(input())
    m = int(input())
    a = [1] * n
    for i in list(map(int, input().split())):
        a[i - 1] = 0
    k = int(input())
    ans = 0
    l = 0
    cnt0 = 0
    for r, v in enumerate(a):
        cnt0 += 1 - v
        while cnt0 > k:
            cnt0 -= 1 - a[l]
            l += 1
        ans = max(ans, r - l + 1)
        pass
    print(ans)


if __name__ == "__main__":
    main()
