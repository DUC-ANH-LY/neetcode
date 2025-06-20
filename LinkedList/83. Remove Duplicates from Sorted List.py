# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # original solution
        cnt = Counter() 
        cur1 = head
        res = ListNode() 
        cur = res
        while cur1:
            if cur1.val not in cnt:
                cnt[cur1.val]  += 1
                cur.next = ListNode(cur1.val) 
                cur = cur.next
            cur1 = cur1.next
        return res.next 

        # shorter
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head