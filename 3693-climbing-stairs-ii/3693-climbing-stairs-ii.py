class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs=[0]+costs
        dp=[10**12]*(n+1)
        dp[0]=0
        for i in range(n):
            for j in range(1,4):
                k=i+j
                if k<=n:
                    dp[k]=min(dp[k], dp[i]+costs[k]+j*j)
        return dp[n]