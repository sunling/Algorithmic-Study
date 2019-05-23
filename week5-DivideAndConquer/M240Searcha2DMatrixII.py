class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix[0]) == 0:
            return False
        l1, r1, l2, r2 = 0, 0, len(matrix)-1, len(matrix[0])-1
        return self.helper(matrix, l1, r1, l2, r2, target)

    def helper(self, matrix, l1, r1, l2, r2, target):
        if not (0 <= l1 <= l2 and l2 < len(matrix) and 0 <= r1 <= r2 and r2 < len(matrix[0])):
            return False
        mx = l1 + (l2 - l1) // 2
        my = r1 + (r2 - r1) // 2
        if matrix[mx][my] == target:
            return True
        elif matrix[mx][my] < target:
            return self.helper(matrix, l1, my+1, l2, r2, target) or self.helper(matrix, mx+1, r1, l2, r2, target)
        else:
            return self.helper(matrix, l1, r1, l2, my-1, target) or self.helper(matrix, l1, r1, mx-1, r2, target)
