import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_column = [row[0] for row in matrix]
        row_index = bisect.bisect(left_column, target)
        print(row_index)
        if row_index <= 0:
            return False
        col_index = bisect.bisect(matrix[row_index-1], target)
        print(col_index)
        if col_index <= 0:
            return False

        # print(f"row index is {row_index} in {left_column}")
        # print(f"col index received is {col_index} in {matrix[row_index]}")
        # print(f"location is ({row_index-1}, {col_index-1}) in {matrix}")

        return (matrix[row_index-1][col_index-1] == target)