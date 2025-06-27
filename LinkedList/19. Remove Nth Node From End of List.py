# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TC: O(n) 
        # SC: O(n)
        nn = 0
        res = ListNode() 
        res.next = head
        cur = res.next
        while cur:
            nn += 1
            cur = cur.next  
        cur = res
        i = nn - n - 1
        while i >= 0 and cur:
            cur = cur.next 
            i -= 1
        if cur: 
            cur.next = cur.next.next
        return res.next
