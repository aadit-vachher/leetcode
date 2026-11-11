class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        t=min(need1,need2)
        total=t*min(costBoth,cost1+cost2)
        rem1=need1-t
        rem2=need2-t
        total+=rem1*min(cost1,costBoth)
        total+=rem2*min(cost2,costBoth)
        return total