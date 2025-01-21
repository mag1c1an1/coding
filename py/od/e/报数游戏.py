# 约瑟夫环
class People:
    def __init__(self, no):
        self.origin = no
        self.t = False


def main():
    m = int(input())
    len = 100
    l = []
    for i in range(1, 101):
        l.append(People(i))
    i = 0
    cnt = 1
    while len >= m:
        if l[i % 100].t == True:
            i += 1
            continue
        if cnt == m:
            l[i % 100].t = True
            cnt = 1
            len -= 1
            i += 1
            continue
        cnt += 1
        i += 1

    ans = []
    for p in l:
        if p.t:
            continue
        ans.append(p.origin)
    print(",".join(map(str,ans)))


if __name__ == "__main__":
    main()
