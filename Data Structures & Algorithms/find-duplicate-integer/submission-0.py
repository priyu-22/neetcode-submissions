class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # conditions: nums array contains exactly n+1 i.e len of nums
        # and integers in nums are in range [1,n] i.e 1,...,n
        # exactly 1 integer repeated for sure
        # this is a linked list problem. the number in nums array points to the index with that number i.e 1 points to nums[1]
        # as there will only 1 number repeated, we can say it created a cycle in linked list. i.e multiple numbers points at same index
        # hence this can be solved by floyd's algorithm (cycle detection)

        fast, slow = 0, 0
        # loop 1: break when fast == slow
        while True:
            slow = nums[slow] # increase by 1
            fast = nums[nums[fast]] #increase by 2
            if fast == slow:
                break
        
        # now to exactly get which node starts cycle; start loop 2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow # the node which starts cycle is the same number which is repeated in input array