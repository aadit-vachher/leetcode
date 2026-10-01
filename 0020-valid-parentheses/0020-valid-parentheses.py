class Solution(object):
    def isValid(self, s):
        stack=[]
        bracket={'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i] in bracket:
                stack.append(s[i])
            elif len(stack)!=0 and s[i]==bracket[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack)==0
        
       