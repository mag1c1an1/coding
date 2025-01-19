def main():
    puzz = list(map(lambda s: "".join(sorted(set(s))), input().split(",")))
    origin = input().split(',')
    bank = origin[:]
    bank = list(map(lambda s: "".join(sorted(set(s))),bank))
    ans = []
    for w in puzz:
        f = False
        for i,b in enumerate(bank):
            if b == w:
                ans.append(origin[i])
                f = True
                break
        if not f:
            ans.append("not found")
    print(",".join(ans))


if __name__ == "__main__":
    main()
