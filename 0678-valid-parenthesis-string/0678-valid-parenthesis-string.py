class Solution:
    def checkValidString(self, s: str) -> bool:
        mini=0
        maxi=0
        for i in s:
            if i=="(":
                mini+=1
                maxi+=1
            elif i==")":
                mini-=1
                maxi-=1
            else:
                mini-=1
                maxi+=1
            if maxi<0:
                return False
            if mini<0:
                mini=0
        if mini==0:
            return True
        else:
            return False
            