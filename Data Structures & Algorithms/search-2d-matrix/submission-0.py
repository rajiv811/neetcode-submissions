class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Run 2 binary searches:
        1) search through top to bottom rows to eliminate rows w/o target
        2) search through row to find if target is within that row
        """
        ROWS,COLS = len(matrix), len(matrix[0])
        top,bottom = 0,ROWS-1

        while top <= bottom:
            mid = (top+bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        l,r = 0, COLS-1
        ans_row = (top+bottom) // 2
        while l<=r:
            mid = (l+r) // 2
            if matrix[ans_row][mid] < target:
                l = mid + 1
            elif matrix[ans_row][mid] > target:
                r = mid - 1
            else:
                return True
        return False
