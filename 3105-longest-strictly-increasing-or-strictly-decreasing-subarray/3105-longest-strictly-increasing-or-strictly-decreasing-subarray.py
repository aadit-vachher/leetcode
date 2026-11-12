class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l2=[]
        l3=[]
        l4=[]
        for i in range(len(nums)):
            l1=nums
            for j in range(i,len(nums)):
                l1=nums[i:j+1]
                l2.append(l1)
        print(l2)
        for i in l2:
            x=sorted(i)
            s=sorted(set(i))
            if i==s or i==s[::-1]:
                l3.append(len(i))
            # else:
            #     l3.append(0)
        return max(l3)