class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Hashmap O(n) not much intuitive 
        # TC: O(N) 
        # SC:  O(N)
        cnt = Counter() 
        tmp = 0 
        res = 0
        for num in nums:
            tmp += num
            if tmp == goal:
                res += 1 
            if tmp - goal in cnt:
                res += cnt[tmp - goal]
            cnt[tmp] += 1
        return res

        # Sliding window, better understand and more familiar
        # TC: O(N) 
        # SC: O(1) 
        def slideAtMost(gg):
            l, n = 0, len(nums)
            tmp, res = 0, 0
            for r in range(n):
                tmp += nums[r] 
                while tmp > gg and l <= r:
                    tmp -= nums[l] 
                    l += 1
                # for all subarray counting 
                res += (r - l + 1)
            return res

        return slideAtMost(goal) - slideAtMost(goal - 1)