class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                #save the topLeft
                topLeft = matrix[top][l + i]
                
                #move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                #move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                #move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                #move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
            """ Here is the explanation for the code above:
1. Create two pointers, l and r, which indicate the leftmost and rightmost columns of the matrix, respectively. 
    The goal is to rotate the matrix by swapping the corners of each square, starting from the outermost square.
2.  The while loop continues until l > r, meaning that the left and right pointers have met.
3.  The for loop is used to iterate through the elements of the current square.
4.  The top and bottom pointers are used to indicate the current top and bottom rows of the current square, respectively.
5.  top_left is used to save the value of the top left corner of the current square.
6.  The top left corner is replaced with the bottom left corner.
7.  The bottom left corner is replaced with the bottom right corner.
8.  The bottom right corner is replaced with the top right corner.
9.  The top right corner is replaced with the top left corner.
10. The top and bottom pointers are incremented and decremented, respectively.
11. The left and right pointers are incremented and decremented, respectively. """
                
            