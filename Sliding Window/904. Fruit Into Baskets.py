from collections import *
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # this problems as same as find max len of subarray with exactly 2 diff number
        l, cnt = 0, Counter() 
        n = len(fruits) 
        res = 0
        for r in  range(n): 
            cnt[fruits[r]] += 1 
            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del cnt[fruits[l]] 
                l += 1 
            res = max(res, r - l + 1)
        return res 