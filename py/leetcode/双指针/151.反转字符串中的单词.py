class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        n = len(s)
        l = r = n - 1
        res = []
        w = True
        while l >= 0:
            while l >= 0 and s[l] != " ":
                l -= 1
            res.append(s[l + 1 : r + 1])
            while l >= 0 and s[l] == " ":
                l -= 1
            r = l
        return " ".join(res)
