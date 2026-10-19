class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total = 0
        min_arr = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_arr = min(r-l+1, min_arr)
                total -= nums[l]
                l+=1
        return 0 if min_arr == float('inf') else min_arr
