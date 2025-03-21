class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数

        @cache
        def dfs(r):
            ret = False
            if r < 0:
                return True
            for l in range(r, max(r - max_len, -1), -1):
                if s[l : r + 1] in st:
                    ret = ret or dfs(l - 1)
            return ret

        return dfs(len(s) - 1)

    def wordBreak_f(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        st = set(wordDict)
        n = len(s)
        f = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if f[j] and s[j:i] in st:
                    f[i] = True
                    break
        return f[n]
