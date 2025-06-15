class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, n = 0, len(s2) 
        cnt = Counter(s1) 
        def check(a):
            for k in cnt:
                if a == 0:
                    if cnt[k] != 0:
                        return False
                elif a ==  1:
                    if cnt[k] < 0:
                        return False
            return True
        
        res = False
        for r in range(n):
            if s2[r] in cnt:
                cnt[s2[r]] -= 1
                while not check(1):
                    cnt[s2[l]] += 1
                    l += 1
                if check(0):
                    res = True 
                    break
            else:
                cnt = Counter(s1) 
                l = min(n, r+1)
        return res