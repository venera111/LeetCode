# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #если нет узлов, деревья равны
            return True
        if p and q and p.val == q.val: #проверка существования узлов и их равенство
            #в стеке функция с левыми нодами, затем функция с правыми
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        