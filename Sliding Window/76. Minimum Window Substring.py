class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # TC: O(26n) 
        # SC: O(26) 
        l = 0 
        cnt = Counter(t) 
        n = len(s) 
        tmp = Counter() 
        res = ""
        def check():
            c = 0
            for k in tmp:
                if k in cnt: 
                    if tmp[k] < cnt[k]:
                        return False 
                    c += 1
            return c == len(cnt)
        for r in  range(n):
            tmp[s[r]] += 1
            while check():
                if (res == "" or len(res) > (r-l+1)): 
                    res = s[l:r+1] 
                tmp[s[l]] -= 1
                l += 1 
            
        return res                 