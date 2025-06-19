class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TC: O(N) 
        # SC: O(N) -> can be reduce to O(1) by using 1 variable 
        l, n, res, cnt = 0, len(nums), 0, Counter() 
        
        for r in range(n):
            cnt[nums[r]] += 1
            while r - l + 1 - cnt[1] > k:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1 
            res = max(res, r -l + 1)
        return res