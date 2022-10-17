# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = '',''
        while l1 or l2:
            if l1:
                n1 = str(l1.val) + n1
                l1 = l1.next
            if l2:
                n2 = str(l2.val) + n2
                l2 = l2.next
            
        
        summ = list(str(eval(n1+'+'+n2)))
        ans = curr = ListNode(0)
        while summ:
            curr.next = ListNode(val=int(summ.pop()))
            curr = curr.next
        return ans.next