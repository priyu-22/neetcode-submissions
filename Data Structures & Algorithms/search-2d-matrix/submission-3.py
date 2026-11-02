class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row which could have target
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bott = 0, ROWS-1
        while top <= bott:
            mid = (top+bott)//2
            if target > matrix[mid][-1]: # last element of the row
                top = mid+1
            elif target < matrix[mid][0]: # first element of the row
                bott = mid-1
            else:
                break # target is exactly in the range of current row
        # if no valid row found then return false
        if not(top <= bott):
            return False

        l, r = 0, COLS -1
        while l<=r:
            m = (l+r)//2
            if target == matrix[mid][m]:
                return True
            else:
                if target > matrix[mid][m]:
                    l = m+1
                else:
                    r = m-1
        return False
            