class Solution:
    def canAliceWin(self, n: int) -> bool:
        ctr = 10
        a = True
        while n >= ctr:
            n -= ctr
            a = not a
            ctr -= 1
        return not a