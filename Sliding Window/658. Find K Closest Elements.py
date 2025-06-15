class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sliding Window O(n)
        l, n = 0, len(arr)
        
        res = []    
        check = False
        for r in range(n):
            res.append(arr[r])
            while len(res) > k:
                if abs(arr[l] - x) > abs(arr[r] - x):
                    res.pop(0) 
                    l += 1
                else:
                    res.pop()
        return res
        
