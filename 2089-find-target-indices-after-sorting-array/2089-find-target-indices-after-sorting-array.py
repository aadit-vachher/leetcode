class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ctr = 0
        less = 0
        for i in nums:
            if i <= target:
                ctr += 1
            if i < target:
                less += 1
        return list(range(less, ctr))