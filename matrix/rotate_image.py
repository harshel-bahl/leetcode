# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

from typing import List

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        - Can be transposed, then cols swapped horizontally
        """

        rows, cols = len(matrix), len(matrix[0])

        startCol = 0
        for i in range(rows):
            for j in range(startCol, cols):

                origVal = matrix[i][j]
                targetVal = matrix[j][i]

                matrix[i][j] = targetVal
                matrix[j][i] = origVal
            
            startCol += 1

        for i in range(rows):
            matrix[i] = [matrix[i][x] for x in range(cols-1, -1, -1)]

        return matrix    

solution = Solution()

print(solution.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]]))