class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ctr = 0
        x = 0
        
        for i in s:
            if i == '(':
                ctr += 1
            else:
                if ctr > 0:
                    ctr -= 1
                else:
                    x += 1
                    
        return x + ctr