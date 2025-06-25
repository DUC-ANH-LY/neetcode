# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        hm = Counter() 
        while headA:
            hm[headA] += 1
            headA = headA.next
        while headB:
            if headB  in hm: 
                return headB
            hm[headB] += 1
            headB = headB.next
        return None 
                
        