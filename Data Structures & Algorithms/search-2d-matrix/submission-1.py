class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                l, r = col, len(matrix[row])-1
                if target == matrix[row][l] or target == matrix[row][r]:
                    return True
                if target < matrix[row][r] and target > matrix[row][l]:
                    m = (r+l)//2
                    if target == matrix[row][m]:
                        return True
                    elif target > matrix[row][m]:
                        l += m
                    else:
                        r -= m
        return False