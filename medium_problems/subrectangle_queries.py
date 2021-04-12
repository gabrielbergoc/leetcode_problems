# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:
#
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
#
# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)
#
# Returns the current value of the coordinate (row,col) from the rectangle.

# https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries:

    def __init__(self, rectangle: list):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.matrix[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


print()
print('Testing example #1:')
mat = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print('Inicial matrix:\n\
[[1,2,1],\n'
'[4,3,4],\n'
'[3,2,1],\n'
'[1,1,1]]\n')
print('getValue(0, 2)')
print('Expected: 1')
print('Answer:', mat.getValue(0, 2), '\n')
mat.updateSubrectangle(0, 0, 3, 2, 5)
print('updateSubrectangle(0, 0, 3, 2, 5)')
print('getValue(0, 2)')
print('Expected: 5')
print('Answer:', mat.getValue(0, 2), '\n')
print('getValue(3, 1)')
print('Expected: 5')
print('Answer:', mat.getValue(3, 1), '\n')
mat.updateSubrectangle(3, 0, 3, 2, 10)
print('updateSubrectangle(3, 0, 3, 2, 10)')
print('getValue(3, 1)')
print('Expected: 10')
print('Answer:', mat.getValue(3, 1), '\n')
print('getValue(0, 2)')
print('Expected: 5')
print('Answer:', mat.getValue(0, 2))
print()

print()
print('Testing example #2:')
mat = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
print('Inicial matrix:\n\
[[1,1,1],\n'
'[2,2,2],\n'
'[3,3,3]]\n')
print('getValue(0, 0)')
print('Expected: 1')
print('Answer:', mat.getValue(0, 0), '\n')
mat.updateSubrectangle(0, 0, 2, 2, 100)
print('updateSubrectangle(0, 0, 2, 2, 100)')
print('getValue(0, 0)')
print('Expected: 100')
print('Answer:', mat.getValue(0, 0), '\n')
print('getValue(2, 2)')
print('Expected: 100')
print('Answer:', mat.getValue(2, 2), '\n')
mat.updateSubrectangle(1, 1, 2, 2, 20)
print('updateSubrectangle(1, 1, 2, 2, 20)')
print('getValue(2, 2)')
print('Expected: 20')
print('Answer:', mat.getValue(2, 2), '\n')
print()