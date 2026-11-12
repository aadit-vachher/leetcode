class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
        
        # for i in range(len(l2)):
        #     f=0
        #     ctr=0
        #     if len(l2[i])==1:
        #         l3.append(1)
        #     else:
        #         for j in range(len(l2[i])-1):
                    
        #             # ctr=0
        #             if l2[i][j]<l2[i][j+1]:
        #                 f=1
        #                 ctr+=1
        #             else:
        #                 f=0
        #                 break
        #         l3.append(ctr)

        #         l3.append(ctr)

        # print(l3)