class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ctr=0
        dig=0
        for i in range(len(s)):
            if(s[i])=='(':
                dig+=1
            else:
                dig-=1

                if s[i-1]=="(":
                    ctr+=2**dig
        return ctr