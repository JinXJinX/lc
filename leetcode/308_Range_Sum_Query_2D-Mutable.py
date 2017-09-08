
# AC robust solution
# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 242 ms
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = matrix


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        try:
            self.m[row][col] = val
        except:
            pass


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rst = 0
        for r in self.m[row1:row2+1]:
            rst += sum(r[col1:col2+1])
        return rst

# better Solution, reduced time of add operations
# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 72 ms
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.m = matrix


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if col == 0:
            old = self.m[row][0]
        else:
            old = self.m[row][col] - self.m[row][col-1]

        change = val - old
        for i in range(col, len(self.m[row])):
            self.m[row][i] += change


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rst = 0
        if col1 == 0:
            for row in self.m[row1:row2+1]:
                rst += row[col2]
        else:
            for row in self.m[row1:row2+1]:
                rst += row[col2] - row[col1-1]
        return rst


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
