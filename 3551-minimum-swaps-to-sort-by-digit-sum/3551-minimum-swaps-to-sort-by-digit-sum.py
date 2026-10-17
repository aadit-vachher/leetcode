class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def func(n):
            return sum(int(d) for d in str(n))
            
        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (func(x), x))
        d1 = {}
        for i in range(n):
            d1[nums[i]] = i
    
        seen = [False] * n
        ctr = 0
        for i in range(n):
            if seen[i] or nums[i] == sorted_nums[i]:
                continue
            size = 0
            j = i
            while not seen[j]:
                seen[j] = True
                next_val = sorted_nums[j]
                j = d1[next_val]
                size += 1
            if size > 1:
                ctr += (size - 1)
        return ctr
            