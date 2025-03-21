# 模拟加法
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        n1, n2 = list(reversed(num1)), list(reversed(num2))

        def tmp(n1, n2):
            if len(n1) < len(n2):
                n1, n2 = n2, n1
            d = abs(len(n1) - len(n2))
            for _ in range(d):
                n2.append("0")

        tmp(n1, n2)

        res = []
        for i in range(len(n1)):
            a = ord(n1[i]) - ord("0")
            b = ord(n2[i]) - ord("0")
            c = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            res.append(str(c))

        if carry != 0:
            res.append(str(carry))

        return "".join(reversed(res))
