class Solution:
    # O(N)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        tmp = 1
        l, n = 0, len(nums) 
        res = 0
        if k <= 1:
            return 0
        for r in range(n):
            tmp *= nums[r]
            while tmp >= k:
                tmp /= nums[l]
                l += 1
            res += (r-l+1)
        return res