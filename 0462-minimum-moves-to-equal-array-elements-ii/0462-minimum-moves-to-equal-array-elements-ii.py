class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        nikku=nums[len(nums)//2]
        tot=0
        for i in nums:
            tot+=abs(i-nikku)
        return tot