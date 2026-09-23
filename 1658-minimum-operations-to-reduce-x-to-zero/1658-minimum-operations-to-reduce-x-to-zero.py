class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tar, n = sum(nums) - x, len(nums)
        if tar == 0:
            return n
        maxx = curr = left = 0
        for right, val in enumerate(nums):
            curr += val
            while left <= right and curr > tar:
                curr -= nums[left]
                left += 1
            if curr == tar:
                maxx = max(maxx, right - left + 1)
        
        return n - maxx if maxx else -1