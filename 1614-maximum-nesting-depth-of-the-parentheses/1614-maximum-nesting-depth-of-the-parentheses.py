class Solution:
    def maxDepth(self, s: str) -> int:
        max1=0
        ctr=0
        for i in s:
            if i=='(':
                ctr+=1
            elif i==')':
                ctr-=1
            max1=max(max1,ctr)
        return max1
