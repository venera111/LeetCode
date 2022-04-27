class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for arr in matrix:
            if target <= arr[n-1]:
                for k in arr:
                    if target == k:
                        return True
        return False