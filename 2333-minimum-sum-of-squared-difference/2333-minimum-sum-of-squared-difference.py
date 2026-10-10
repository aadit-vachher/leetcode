class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(d) <= k:
            return 0
        cnt = [0] * (max(d) + 1)
        for x in d:
            cnt[x] += 1
        m = len(cnt) - 1
        while k:
            while m and cnt[m] == 0:
                m -= 1
            c = cnt[m]
            if c <= k:
                k -= c
                cnt[m - 1] += c
                cnt[m] = 0
            else:
                cnt[m] -= k
                cnt[m - 1] += k
                k = 0
        return sum(i * i * c for i, c in enumerate(cnt))