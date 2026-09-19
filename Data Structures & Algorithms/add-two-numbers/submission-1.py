# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()

        while l1 or l2:
            if l1 and l2:
                new_val = l1.val + l2.val
            elif l1:
                new_val = l1.val
            else:
                new_val = l2.val
            
            if new_val > 9:
                res.val += new_val - 10
                res.next = ListNode(1)
            elif new_val == 9 and res.val == 1:
                res.val = 0
                res.next = ListNode(1)
            else:
                res.val += new_val
                res.next = ListNode()
            prev = res
            res = res.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        print(res.val)
        if l1:
            res.val = l1.val
            res.next = l1.next
            print("a")
        elif l2:
            res.val = l2.val
            res.next = l2.next
            print("b")
        else:
            if res.val == 0:
                prev.next = None

        return head