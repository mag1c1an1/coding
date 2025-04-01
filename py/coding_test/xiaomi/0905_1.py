# 小A每天都要吃a,b两种面包各一个。而他有n个不同的面包机，不同面包机制作面包的时间各不相同。第i台面包机制作a面包需要花费ai的时间，制作b面包则需要花费bi的时间。为能尽快吃到这两种面包，小A可以选择两个不同的面包机x,y同时工作，并分别制作a,b两种面包，花费的时间将是max(ax,by)。当然，小A也可以选择其中一个面包机x制作a,b两种面包，花费的时间将是ax+bx。为能尽快吃到面包，请你帮小A计算一下，至少需要花费多少时间才能完成这两种面包的制作。
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ma, mb = float("inf"), float("inf")
mai, mbi = -1, -1
for i in range(n):
    if a[i] < ma:
        ma = a[i]
        mai = i
    if b[i] < mb:
        mb = b[i]
        mbi = i
if mai != mbi:
    print(max(ma, mb))
else:
    second = float("inf")
    for i in range(n):
        if i != mai:
            second = min(second, max(a[i], mb))
            second = min(second, max(b[i], ma))
    print(min(ma + mb, second))
