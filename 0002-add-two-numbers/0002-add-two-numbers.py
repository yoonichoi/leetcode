# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        exp = 0
        while l1:
            n1 += l1.val * 10**exp
            exp += 1
            l1 = l1.next
        exp = 0
        while l2:
            n2 += l2.val * 10**exp
            exp += 1
            l2 = l2.next
        num = list(str(n1+n2))
        ans = curr = ListNode(0)
        while num:
            n = int(num.pop())
            curr.next = ListNode(n)
            curr = curr.next
        return ans.next
        