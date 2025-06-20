# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # hashmap 
        # TC: O(n) 
        # SC: O(n)
        cur = head
        seen = set()
        while cur:
            cur = cur.next
            if cur in seen:
                return True  
            seen.add(cur)
        return False 

        #  floyd detect cycle 
        #  TC: O(n) 
        #  SC: O(1)
        #  https://cp-algorithms.com/others/tortoise_and_hare.html
        
        slow, fast = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
        