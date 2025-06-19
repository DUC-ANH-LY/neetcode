from sortedcontainers import SortedList
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        # brute force O(n^2) 
        # BST O(nlogk)
        st = SortedList()
        for i in range(len(nums)):
            if i > k: 
                st.remove(nums[i - k - 1])
            p1, p2 = st.bisect_left(nums[i] - t), st.bisect_right(nums[i] + t) 
            if p1 != p2 and p1 != len(nums):
                return True
            st.add(nums[i])
        return False
            