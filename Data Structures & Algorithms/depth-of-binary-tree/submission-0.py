# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS
        max_depth = 0
        if not root:
            return max_depth
        queue = deque([(root, 1)])

        while queue:
            node, layer = queue.popleft()
            max_depth = layer

            if node.left:
                queue.append((node.left, layer + 1))
            if node.right:
                queue.append((node.right, layer + 1))

        return max_depth