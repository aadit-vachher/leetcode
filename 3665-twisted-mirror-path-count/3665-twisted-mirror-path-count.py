class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        I, J = len(grid), len(grid[0])
        dp = [[{'r': 0, 'd': 0} for _ in range(J+1)] for _  in range(I+1)]

        dp[0][0]['r'] = dp[0][0]['d'] = 1

        for i in range(I):
            for j in range(J):
                if i==0 and j==0:
                    continue
                if grid[i][j] == 0:
                    dp[i][j]['r'] = dp[i][j-1]['r'] + dp[i-1][j]['d']
                    dp[i][j]['d'] = dp[i][j-1]['r'] + dp[i-1][j]['d']
                else:
                    dp[i][j]['r'] = dp[i-1][j]['d']
                    dp[i][j]['d'] = dp[i][j-1]['r']

        return dp[-2][-2]['r'] % (10**9 + 7)

        