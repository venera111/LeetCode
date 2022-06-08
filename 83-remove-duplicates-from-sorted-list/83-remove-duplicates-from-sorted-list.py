# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr.next: #итерация по списку до конца
            if curr.val == curr.next.val: #текущий равен следующему
                curr.next = curr.next.next #удаляем слеюущий элемент-дубликат
            else:
                curr = curr.next #если не дубликат, итерируемся
        return head