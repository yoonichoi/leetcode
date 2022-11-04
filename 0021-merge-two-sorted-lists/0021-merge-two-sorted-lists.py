# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        while list1 and list2:
            v1, v2 = list1.val, list2.val
            if v1 <= v2:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr=curr.next
                list2 = list2.next
        if list1 or list2:
            curr.next = list1 if list1 else list2
            curr = curr.next
        return head.next