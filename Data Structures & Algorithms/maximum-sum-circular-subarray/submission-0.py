class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxSum, minSum = nums[0], nums[0]
        curMax, curMin = 0, 0
        for n in nums:
            # max
            curMax= max(curMax+n, n)
            maxSum= max(curMax, maxSum)
            # min
            curMin= min(curMin+n, n)
            minSum= min(curMin, minSum)
            total += n
        # if all numbers are negative
        if maxSum < 0:
            return maxSum    
        return max(maxSum, total-minSum)
