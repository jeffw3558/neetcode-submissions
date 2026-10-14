# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        val2 = 0
        base = 1
        base1 = 1
        while l1 != None:
            
            val1 += l1.val*base
            base = base*10
            l1=l1.next

        while l2 != None:
            
            val2 += l2.val*base1
            base1 = base1*10
            l2=l2.next

        total = val1 + val2
        pointer = ListNode()
        rest = pointer
        empty = False
        while total != 0:
            curr = total%10
            total = total//10
            pointer.next = ListNode(curr)
            pointer = pointer.next
            empty = True
        return rest.next if empty else rest
    

        

