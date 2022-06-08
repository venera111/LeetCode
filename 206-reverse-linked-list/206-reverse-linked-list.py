# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = None
        while head: #итерация к последней ноде списка
            curr = head #сохраняем указатель на текущую ноду
            head = head.next #делаем шаг к следующей ноде
            curr.next = tmp
            tmp = curr #добавление ноды в перевернутый список
        return tmp