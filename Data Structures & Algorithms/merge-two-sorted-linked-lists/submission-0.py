# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        head = ListNode()  # Dummy node
        curr = head        # Pointer to build new list

        # Merge nodes from both lists in sorted order
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                curr.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
            else:
                curr.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
            curr = curr.next  # Move to newly added node

        # Append the remaining nodes (only one of these loops will run)
        while pointer1:
            curr.next = ListNode(pointer1.val)
            pointer1 = pointer1.next
            curr = curr.next

        while pointer2:
            curr.next = ListNode(pointer2.val)
            pointer2 = pointer2.next
            curr = curr.next

        return head.next  # Skip dummy node