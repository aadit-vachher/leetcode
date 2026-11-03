class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x=max(nums)
        ctr=0
        for i in nums:
            ctr+=abs(i-x)
        return ctr