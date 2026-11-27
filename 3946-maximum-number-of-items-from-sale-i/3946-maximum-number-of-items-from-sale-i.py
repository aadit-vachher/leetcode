class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        facs = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    facs[i] += 1
        dp = [float('-inf')] * (budget + 1)
        dp[0] = 0
        for i in range(n):
            p = items[i][1]
            for c in range(budget, p - 1, -1):
                dp[c] = max(dp[c], dp[c - p] + facs[i] + 1)
            for c in range(p, budget + 1):
                if dp[c - p] != float('-inf'):
                    dp[c] = max(dp[c], dp[c - p] + 1)

        return max(dp)