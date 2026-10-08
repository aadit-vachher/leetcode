class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=''
        ctr=0
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i=='(':
                    stack.append(i)
                    ans+='('
                else:
                    stack.pop()
                    if stack:
                        ans+=')'
        return ans

