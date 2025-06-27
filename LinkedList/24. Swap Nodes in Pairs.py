# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TC: O(n) 
        # SC: O(n)
        res = ListNode() 
        res.next = head
        pre = res
        cur = res.next
        while cur and cur.next: 
            adjNode, nxt = cur.next, cur.next.next
            pre.next = adjNode
            adjNode.next = cur 
            cur.next = nxt
            pre = cur
            cur = cur.next
        return res.next