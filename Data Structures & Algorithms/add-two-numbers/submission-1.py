# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry: #EDGE CASE: if carry is not null or 0 we want to keep adding it to the sum
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            res = val1 + val2 + carry
            # update carry and res
            carry = res // 10 # this gives the carry bit
            res = res % 10 # this gives the unit place number
            curr.next = ListNode(res)

            # update pointers
            curr = curr.next
            # if l1 or l2 are null then there will be no next pointer
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next