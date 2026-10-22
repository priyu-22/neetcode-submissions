# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f, s = head, head
        p = None
        # we need to find half node of the list
        while f and f.next:
            f = f.next.next
            # for slow pointer we want to reverse the first half of the linked list
            temp = s.next
            s.next = p
            p = s
            s = temp
        # at this point s will me start of right side of the list
        # p will be start of left side of the list
        # s and p both will be of same length
        res = 0
        while s:
            #update the res by calculating sum
            res = max(res, (s.val+p.val))
            s = s.next
            p = p.next
        return res