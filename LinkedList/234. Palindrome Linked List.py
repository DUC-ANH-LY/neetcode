# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) 
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]