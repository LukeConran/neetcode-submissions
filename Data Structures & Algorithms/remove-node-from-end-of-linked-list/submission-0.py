# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        print(length)

        curr = head
        if length - n == 0:
            return head.next

        for i in range(length - n - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head