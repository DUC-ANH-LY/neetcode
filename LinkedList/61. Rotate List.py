# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TC: O(n) 
        # SC: O(n)
        if not head:
            return None
        n =  0
        cur = head
        # find the lenght of linked list
        while cur:
            cur = cur.next
            n += 1
        newtail = head 

        # find the newtail by formula, for k < n  n-k, k > n -> n - (k% n) 
        i = n - (k%n)
        while i - 1: 
            newtail = newtail.next
            i -= 1
        # if newtail is not the tail of original linkedlist
        if newtail.next:
            newhead = newtail.next 
            newtail.next = None 
            cur = newhead
            while cur.next:
                cur = cur.next
            cur.next = head 
            return newhead
        return head 