class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]**2
        # else:

        #     l1=[1,len(nums)]
        #     for i in range(2,int(len(nums)//2+1)):
        #         if len(nums)%i==0:
        #             l1.append(i)
        #     print(l1)
        #     l2=[]
        #     for i in l1:
        #         l2.append(nums[i-1]**2)
        #     print(l2)
        #     return sum(l2)

        result = 0
        for index in range(len(nums)):
            if len(nums) % (index+1) == 0:
                result += nums[index] ** 2
        return result