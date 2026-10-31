# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: # if there are not k nodes in the LL then break
                break
            groupNext = kth.next # as we are going to break the link between kth node and its next node. we record it in groupNext
            # start reversing the linked list till we reach groupNext
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # update the groupPrev node. it should point to kth element
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    # Helper function: get kth element fron the list and cur is head of the list
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr