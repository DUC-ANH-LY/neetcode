# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hashmap: O(n + n) 
        # TC: O(n+n)  
        # cnt = Counter() 
        # cur = head 
        # while cur:
        #     cnt[cur.val] += 1
        #     cur = cur.next

        # cur = head
        # res = ListNode()
        # res.next = head
        # pre = res
        # while cur: 
        #     if cnt[cur.val] > 1:
        #         pre.next = cur.next 
        #     else:
        #         pre = pre.next
        #     cur = cur.next
        # return res.next
        # pre node TC: O(n) 
        # SC: O(1) 
        res = ListNode(0, head)  
        pre = res
        cur = head
        while cur:
            check = 0
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                check = 1
            if check:
                pre.next  = cur.next
            else:
                pre = cur
            cur = cur.next
        return res.next