import heapq

n = int(input())


class Task:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __lt__(self, other):
        return self.end_time < other.end_time


lst = [[] for _ in range(n + 1)]

dq = []

for _ in range(n):
    s, e = map(int, input().split())
    t = Task(s, e)
    lst[s].append(t)

ans = 0
for i in range(1, n + 1):
    while dq and dq[0].end_time < i:
        heapq.heappop(dq)
    for t in lst[i]: 
        heapq.heappush(dq,t)
    if dq:
        ans += 1
        heapq.heappop(dq)

print(ans)
