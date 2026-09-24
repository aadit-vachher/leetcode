class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def func(num):
            return sum(int(d) for d in str(num))
        for i in range(len(nums)):
            if func(nums[i]) == i:
                return i
        return -1