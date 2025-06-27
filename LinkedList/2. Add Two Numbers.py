# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TC: O(n+m)
        # SC: O(max(n,m)) 
        res = ListNode() 
        cur = res
        mem = 0
        # while l1 and l2:
        #     val = (l1.val + l2.val + mem) % 10
        #     mem = (l1.val + l2.val + mem) // 10
        #     cur.next = ListNode(val) 
        #     l1 = l1.next
        #     l2 = l2.next
        #     cur = cur.next
        # while l1: 
        #     val = (l1.val + mem) % 10 
        #     mem = (l1.val + mem) // 10 
        #     cur.next = ListNode(val) 
        #     l1 = l1.next
        #     cur = cur.next
        # while l2: 
        #     val = (l2.val + mem) % 10 
        #     mem = (l2.val + mem) // 10 
        #     cur.next = ListNode(val) 
        #     l2 = l2.next
        #     cur = cur.next
        # if mem:
        #     cur.next = ListNode(mem)

        # shorter version 
        while l1 or l2 or mem:
            x, y = l1.val if l1 else 0, l2.val if l2 else 0
            val = (x + y + mem) % 10
            mem = (x + y + mem) // 10 
            cur.next = ListNode(val) 
            cur = cur.next
            if l1: l1= l1.next
            if l2: l2= l2.next
        return res.next