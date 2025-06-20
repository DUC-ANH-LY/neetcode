# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # O(n+m)
        res = ListNode() 
        cur = res
        l1, l2 = list1, list2 
        while l1 or l2: 
            a = None
            if l1 and l2:
                if l1.val >= l2.val:
                    a =  l2.val
                    l2 = l2.next
                else: 
                    a = l1.val
                    l1 = l1.next
            else:
                if l1:
                    a = l1.val 
                    l1 = l1.next
                else: 
                    a = l2.val 
                    l2 = l2.next     
            cur.next = ListNode(a)
            cur = cur.next
        return res.next 