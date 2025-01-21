def main():
    c = int(input())
    ans = float("inf")
    for _ in range(c):
        a, b = map(int, input().split())
        if b >= 128:
            exp = b & 0x70 >> 4
            mant = b & 0xF
            b = (mant | 0x10) << (exp + 3)
        ans = min(ans, a + b)
    print(ans)


if __name__ == "__main__":
    main()
