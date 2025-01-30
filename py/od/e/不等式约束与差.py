def main():
    tmp = input().split(";")
    n = len(tmp)
    a = []
    for i in range(3):
        a.append(list(map(float, tmp[i].split(","))))
    x = list(map(float, tmp[-3].split(",")))
    b = list(map(float, tmp[-2].split(",")))
    f = tmp[-1].split(",")

    ans1 = True
    ans2 = 0.0

    for i, v in enumerate(a):
        s = 0
        for p, q in zip(v, x):
            s += p * q
        match f[i]:
            case "<=":
                ans1 = s <= b[i]
            case ">":
                ans1 = s > b[i]
            case ">=":
                ans1 = s >= b[i]
            case "=":
                ans1 = s == b[i]
            case "<":
                ans1 = s < b[i]
        ans2 = max(ans2, s - b[i])


    ans1 = "true" if ans1 else "false"
    print(f"{ans1} {int(ans2)}")


if __name__ == "__main__":
    main()
