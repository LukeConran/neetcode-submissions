# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        new_list = None
        new_list_head = None

        if curr1 == None:
                new_list_head = curr2
        elif curr2 == None:
                new_list_head = curr1
        else:
            if curr1.val <= curr2.val:
                new_list_head = curr1
            else:
                new_list_head = curr2

        while curr1 or curr2:
            if curr1 == None:
                new_list = self.append(new_list, curr2)
                curr2 = curr2.next
            elif curr2 == None:
                new_list = self.append(new_list, curr1)
                curr1 = curr1.next
            else:
                if curr1.val <= curr2.val:
                    new_list = self.append(new_list, curr1)
                    curr1 = curr1.next
                else:
                    new_list = self.append(new_list, curr2)
                    curr2 = curr2.next

        return new_list_head

        

    def append(self, new_list, node):
        if new_list:
            new_list.next = node
            new_list = new_list.next
        else:
            new_list = node
        return new_list