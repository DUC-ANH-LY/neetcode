from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """ 
        

        # Bruteforce
        # TC: O(N*m*k) 
        if not s or not words or not words[0]:
            return []

        k = len(words[0]) 
        m = len(words)
        substr_size  = m * k   
        n = len(s) 
        res = []  
        word_cnt = Counter(words)

        for i in range(n - substr_size + 1):
            cp = word_cnt.copy()
            for j in range(i, i + substr_size, k):  # only walk m words
                substr = s[j:j + k] 
                if substr not in cp:
                    break
                cp[substr] -= 1
                if cp[substr] == 0:
                    del cp[substr] 
                    
            if not cp:
                res.append(i)

        return res

        # Sliding window 
        # s = barfoothefoobarman
        # ap1 : 0 - 12 starting index 
        # i = 0, [bar][foo][the]...
        # i = 1, [arf][oot]
        # i = 2, [rfo][oth]  
        # i = 3, [foo][the][foo] <- repeating at i = 0
        # i = 4, [oot] <- repeating at i = 1
        # that why we just need to check in range len of k 

        if not s or not words or not words[0]:
            return []

        k = len(words[0]) 
        m = len(words)
        substr_size  = m * k   
        n = len(s) 
        res = []  
        word_cnt = Counter(words)

        for i in range(k):
            l = i
            word_found = 0 
            win_map = Counter()
            for r in range(l, n, k): 
                substr = s[r:r+k] 
                if substr not in word_cnt: 
                    l = r + k 
                    word_found = 0
                    win_map = Counter()
                    continue 
                # inside word_cnt 
                word_found += 1
                win_map[substr] += 1
                # can't be """"while (word_found > m)"""" cause case 
                # s = wordgoodgoodgoodbestword, words = ["word","good","best","word"], "wordgoodgoodgoodbest" = 5 > 4 but still not good 
                # if using hashmap to check { word: 1, good: 3, best: 1} 
                while win_map[substr] > word_cnt[substr]:
                    win_map[s[l: l + k]] -= 1
                    l += k  
                    word_found -= 1 
                if word_found == m:
                    res.append(l)

        return res
