t = int(input())


def solve(n, m) -> bool:
    def helper(start, end,k,v):
        l = start
        s = 0
        for r in range(start, end+1):
            s += r
            if r-l + 1 == k: 
                if s == v:
                    return True
                s -= l
                l += 1
        return False
    
    t = m // 2 + 1
    avg = n//m + 1
    
    start = max(0,n - t * avg)
    
    ans = "YES" if helper(start,n,m,n) else "NO"
    print(ans)
                
        



for _ in range(t):
    n, m = map(int, input().split())
    solve(n, m)
