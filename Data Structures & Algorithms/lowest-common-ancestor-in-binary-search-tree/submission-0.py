# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = []
        q_list = []

        node = root
        while node != p:
            if p.val < node.val:
                node = node.left
                p_list.append("left")
            else:
                node = node.right
                p_list.append("right")

        node = root
        while node != q:
            if q.val < node.val:
                node = node.left
                q_list.append("left")
            else:
                node = node.right
                q_list.append("right")

        print
        ancestor = root
        for i in range(min(len(p_list), len(q_list))):
            if p_list[i] != q_list[i]:
                break
            else:
                if p_list[i] == "left":
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right


        return ancestor