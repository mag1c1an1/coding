# SPDX-FileCopyrightText: LakeSoul Contributors
#
# SPDX-License-Identifier: Apache-2.0

n = int(input())
m = int(input())


class Item:
    def __init__(self, x, y, shape, val):
        self.x = x
        self.y = y
        self.shape = shape
        self.val = val
    
    def __str__(self):
        return f"item{{{self.x}}}"

    def __repr__(self):
        return f"item{{{self.x} * {self.y}, val={self.val}}}"


v = list(map(int, input().split()))

items = []

for i in range(m):
    x, y = map(int, input().split())
    shape = []
    for _ in range(x):
        shape.append(map(int, input().split()))
    items.append(Item(x, y, shape, v[i]))

print(sum(v))