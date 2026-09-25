# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def revLL(self, head):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_start = curr = prev_head = head
        connector = ListNode()
        first_reverse = True
        
        while True:
            prev_head = curr

            for i in range(k-1):
                if not curr:
                    connector.next = prev_head
                    return new_start
                curr = curr.next

            if not curr:
                connector.next = prev_head
                return new_start
            temp = curr.next
            curr.next = None
            curr = temp

            temp = self.revLL(prev_head)
            connector.next = temp
            connector = temp

            print(connector.val)
            if first_reverse:
                first_reverse = False
                new_start = connector

            for i in range(k-1):
                connector = connector.next

            

