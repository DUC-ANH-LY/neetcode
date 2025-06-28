# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # TC: O(n) 
        # SC: O(n)
        list1, list2 = ListNode(), ListNode()
        cur1, cur2 = list1, list2
        cur = head
        while cur: 
            if cur.val >= x: 
                cur2.next = ListNode(cur.val)  
                cur2 = cur2.next
            else: 
                cur1.next = ListNode(cur.val)  
                cur1 = cur1.next
            cur = cur.next  
        
        cur1.next = list2.next
        return list1.next