"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        node_dict = {None:None}

        while curr:
            copy_node = Node(curr.val)
            node_dict[curr] = copy_node
            curr = curr.next

        curr = head
        while curr:
            copy_node = node_dict[curr]
            copy_node.next = node_dict[curr.next]
            copy_node.random = node_dict[curr.random]
            curr = curr.next

        return node_dict[head]