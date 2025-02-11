nums = list(map(int,input().split()))

stk = []


for n1 in nums:
    gen = False
    s = 0
    j = len(stk) - 1
    for v in range(j, -1, -1):
        s += stk[v]
        if s == n1:
            gen = True
            for _ in range(j, v - 1, -1):
                stk.pop()
            stk.append(2 * n1)
            break

    if gen == False:
        stk.append(n1)

print(" ".join(map(str,reversed(stk))))
