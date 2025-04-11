class Solution:
    def longestValidParentheses_dp(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif (
                    s[i - 1] == ")"
                    and i - dp[i - 1] > 0
                    and s[i - 1 - dp[i - 1]] == "("
                ):
                    v = dp[i - 1 - dp[i - 1] - 1] if i - 1 - dp[i - 1] - 1 >= 0 else 0
                    dp[i] = dp[i - 1] + v + 2
                ans = max(ans, dp[i])

        return ans
    
    
    def longestValidParentheses_stk(self, s: str) -> int:
        ans = 0
        stk = [-1]
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    ans = max(ans,i-stk[-1])
        return ans

    def longestValidParentheses_cnt(self, s: str) -> int:
        n = len(s)
        l,r,ans = 0,0,0
        for i in range(n):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                ans = max(ans,2 * r)
            elif r > l:
                l = r = 0
        l = r = 0
        for i in range(n-1,-1,-1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans,2 * l)
            elif l > r:
                l = r = 0
        return ans 