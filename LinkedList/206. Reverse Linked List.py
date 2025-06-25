# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  O(n)
        if not head: return None 
        l, r = head, head.next
        l.next = None 
        res = None 
        while r:
            nxt = r.next
            r.next = l
            l = r
            r = nxt
                
        return l
