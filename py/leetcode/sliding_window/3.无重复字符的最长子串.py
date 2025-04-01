class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = 0
        w = set()
        for r, c in enumerate(s):
            while c in w:
                w.remove(s[l])
                l += 1
            w.add(c)
            ans = max(ans, r - l + 1)
        return ans
