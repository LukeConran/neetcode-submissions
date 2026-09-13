# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])

        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False

        while pQueue or qQueue:
            pNode = pQueue.popleft()
            qNode = qQueue.popleft()

            if pNode.val != qNode.val:
                return False

            left = 0
            right = 0
            if pNode.left:
                pQueue.append(pNode.left)
                left += 1
            if pNode.right:
                pQueue.append(pNode.right)
                right += 1
            if qNode.left:
                qQueue.append(qNode.left)
                left -= 1
            if qNode.right:
                qQueue.append(qNode.right)
                right -= 1
            if left or right:
                return False

        return True