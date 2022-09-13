# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length+1
        if length == n:
            return head.next
        curr = head
        for i in range(length-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head