# SPDX-FileCopyrightText: LakeSoul Contributors
#
# SPDX-License-Identifier: Apache-2.0
from collections import defaultdict
from typing import Set

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 前i个茶点能够完成的最小精力与订单数

res1 = res2 = 0

cnt = defaultdict(int)


def solve(b: Set[int], cnt):
    ret = b
    for t in b:
        if cnt[t] > 0:
            ret.remove(t)
        else:
            curr = t - 1
            check = 2
            ok = False
            while curr >= 0:
                if cnt[curr] >= check:
                    ok = True
                    break
                else:
                    d = check - cnt[curr]
                    curr -= 1
                    check = d * 2
            if ok:
                ret.remove(t)
                curr = t - 1
                check = 2
                while curr >= 0:
                    if cnt[curr] >= check:
                        cnt[curr] -= check
                        break
                    else:
                        d = check - cnt[curr]
                        curr -= 1
                        check = d * 2
                        cnt[curr] = 0

    return ret


for x in a:
    res1 += 1
    cnt[x] += 1
    b = solve(b, cnt)

if len(b) == 0:
    print(res1)
else:
    print(m-len(b))
