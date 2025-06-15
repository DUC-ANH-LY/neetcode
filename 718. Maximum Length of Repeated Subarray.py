class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force O(n^3)
        n1, n2 = len(nums1), len(nums2)
        res = 0
        for i in range(n1): 
            for j in range(n2): 
                k = 1
                while i + k <= n1 and j + k <= n2 and nums1[i:i+k] == nums2[j:j+k]: 
                        k += 1    
                res = max(res, k - 1) 
        return res

        # dynamic programming top down
        # O(3^n+m) topdown, @cache for memo but mem limit 
        res = 0
        @cache 
        def f(i,j):
            nonlocal res 
            if i >= n1 or j >= n2:
                return 0
            f(i+1, j)
            f(i, j+1)
            ans = 1 + f(i+1, j+1) if nums1[i] == nums2[j] else 0
            res = max(res, ans)
            return ans
        f(0,0)
        return res


        # dp bottom up 
        # O(nm)
        res = 0
        dp = [[ 0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1-1 , -1, -1):
            for j in range(n2-1,-1 , -1):
                dp[i][j] = 1 + dp[i+1][j+1] if nums1[i] == nums2[j] else 0
                res = max(res, dp[i][j])
        return res
