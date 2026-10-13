class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x*x)
        l=0
        r=len(nums)-1
        score=0
        sign=1
        while l<=r:
            if sign==1:
                score+=nums[r]**2
                r-=1
            else:
                score-=nums[l]**2
                l+=1
            sign*=-1
        return score
        