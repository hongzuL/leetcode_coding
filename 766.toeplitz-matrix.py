#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        matrix_val = []
        # create a matrix with 0s
        for row in range(n_row):
            matrix_val.append([0]*n_col)
        # go through each element in the matrix
        for row in range(n_row):
            for col in range(n_col):
                # if the element is the first element:
                if row == 0 or col == 0:
                    matrix_val[row][col] = 1
                else:
                    if matrix_val[row-1][col-1] == 1 and matrix[row][col] == matrix[row-1][col-1]:
                        matrix_val[row][col] = 1
                    if col == n_col-1:
                        if matrix_val[row][col] == 0:
                            return False
                    if row == n_row-1:
                        if matrix_val[row][col] == 0:
                            return False
        return True
# @lc code=end

