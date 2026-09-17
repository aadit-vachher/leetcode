class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        curr_sum = 0
        left = 0
        ans = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                length = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, length + min_len[left - 1])
                
                if right > 0:
                    min_len[right] = min(min_len[right - 1], length)
                else:
                    min_len[right] = length
            else:
                if right > 0:
                    min_len[right] = min_len[right - 1]
                    
        return ans if ans != float('inf') else -1