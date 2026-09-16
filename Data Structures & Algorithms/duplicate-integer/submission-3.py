class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        for i in nums:
            if i in dupe:
                return True
            dupe.add(i)
        return False