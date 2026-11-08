class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap for already checked values
        checked = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in checked:
                return [checked[val], i]
            checked[n] = i
        return []