class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in seen:
                return [seen[ans], i]
            seen[num] = i
        return []