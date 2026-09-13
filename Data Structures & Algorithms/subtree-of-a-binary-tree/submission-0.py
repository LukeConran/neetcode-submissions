# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()
            is_sub_tree = self.checker(node, subRoot)
            if is_sub_tree:
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def checker(self, big_tree, sub_tree):
        sub_queue = deque([sub_tree])
        big_queue = deque([big_tree])

        while sub_queue:
            big_node, sub_node = big_queue.popleft(), sub_queue.popleft()
            if big_node.val != sub_node.val:
                return False
            if (big_node.left and not sub_node.left) or (not big_node.left and sub_node.left):
                return False
            if (big_node.right and not sub_node.right) or (not big_node.right and sub_node.right):
                return False

            if sub_node.left:
                sub_queue.append(sub_node.left)
                big_queue.append(big_node.left)
            if sub_node.right:
                sub_queue.append(sub_node.right)
                big_queue.append(big_node.right)

        return True

