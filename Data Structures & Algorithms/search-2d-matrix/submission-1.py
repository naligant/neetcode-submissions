class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        while i < len(matrix) and j < len(matrix[0]):
            if i == len(matrix)-1:
                j = 0
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                return False
            print(i)
            print(len(matrix)-1)
            if matrix[i][len(matrix[0])-1] < target:
                i += 1
                continue
            else:
                j = 0
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                return False
