# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        dummy = head
        while curr != None:
            dummy = dummy.next
            curr.next = prev
            prev = curr
            curr = dummy
        head = prev
        return head   



        
        
        
        

        

