class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isFound = False
        for lst in matrix:
            isFound = self.binarySearch(lst, target)
            if isFound:
                return True
        return isFound

    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            else:
                if nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        return False 