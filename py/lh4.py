# SPDX-FileCopyrightText: LakeSoul Contributors
#
# SPDX-License-Identifier: Apache-2.0
# m is col, n = row
from collections import deque


n, m = map(int, input().split())

def check(g):
    global n, m
    start = Point(0, 0)
    end = Point(m - 1, n - 1)
    dq = deque([start])
    ret = False
    while len(dq):
        p = dq.popleft()
        if p == end:
            return True
        v = g[p.y][p.x]
        nx, ny = p.x, p.y
        if v == 1:
            ny += 1
        elif v == 2:
            ny -= 1
        elif v == 3:
            nx += 1
        elif v == 4:
            nx
        elif v == 5:
            pass
        elif v == 6:
            pass
        else:
            # 7
            pass
        if 0 <= nx < m and 0 <= ny < n:
            dq.append(Point(nx, ny))

    return ret


def turn(g, col):
    global n, m
    tmp = g[n - 1][col]
    for i in range(0, n - 1):
        g[i + 1][col] = g[i][col]
    g[0][col] = tmp


class State:
    def __init__(self, times, g):
        self.times = times
        self.g = g


ans = 0

print(m)
