# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr=head
        array=[]
        while curr.next!=None:
            array.append(curr.val)
            curr=curr.next
        array.append(curr.val)
        array.reverse()
        curr=head
        for ele in array:
            curr.val=ele
            curr=curr.next
        return head
            