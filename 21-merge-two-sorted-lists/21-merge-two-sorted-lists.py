# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if list1 is None:
                return list2
            return list1
        curr1, curr2 = list1, list2
        if list1.val <= list2.val:
            curr1.next = self.mergeTwoLists(list1.next, list2)
            return curr1
        curr2.next = self.mergeTwoLists(list1, list2.next)
        return curr2
        