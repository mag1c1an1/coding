s = list(input().split())


def is_digit(c):
    return ord("0") <= ord(c) <= ord("9")


res = [[], []]

pre = 0


for piece in s:
    n, t = piece[0], piece[-1]
    if not is_digit(n):
        print("ERROR")
        exit()
    if t != "N" and t != "Y":
        print("ERROR")
        exit()

    if t == "Y":
        res[pre].append(n)
    else:
        pre = 1 - pre
        res[pre].append(n)

res[0].sort()
res[1].sort()


if len(res[0]) == 0 or len(res[1]) == 0:
    if res[0]:
        print(" ".join(res[0]))
    if res[1]:
        print(" ".join(res[1]))
    exit()

if res[0][0] < res[1][0]:
    print(" ".join(res[0]))
    print(" ".join(res[1]))
else:
    print(" ".join(res[1]))
    print(" ".join(res[0]))
