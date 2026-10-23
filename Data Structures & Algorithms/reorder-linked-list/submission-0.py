# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # common mistake: after finding middle, we want to break link between middle and next of middle to make 2 linked lists. we can do that by making slow.next = None
        second = slow.next # keep it in another variable before breaking link
        prev = slow.next = None
        # reverse second part
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev has head of second linked list which is reversed half of the input
        # merge both parts
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first , second = tmp1, tmp2