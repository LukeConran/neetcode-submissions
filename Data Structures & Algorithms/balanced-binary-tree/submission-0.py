# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def checkNode(root):
            nonlocal isBalanced
            if not root:
                return 0

            # print(root.val)

            if not root.right:
                hR = 0
            else:
                hR = checkNode(root.right) + 1
            if not root.left:
                hL = 0
            else:
                hL = checkNode(root.left) + 1

            if abs(hL - hR) > 1:
                isBalanced = False
                
            return max(hR, hL)

        checkNode(root)
        return isBalanced

        