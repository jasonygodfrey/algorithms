class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
    
    """ Here is the explanation for the code above:
1. First we check if the grid is empty or not. If it is empty we return 0.
2. Then we find the number of rows and columns in the grid.
3. We create a set to keep track of the visited cells.
4. We create a variable to count the number of islands.
5. We create a function to perform a breadth first search from a given cell.
6. We start a for loop to iterate over the rows.
7. We start a for loop to iterate over the columns.
8. We check if the current cell is a land cell and if it has been visited or not.
9. If the current cell is a land cell and it has not been visited we perform a breadth first search from the current cell.
10. We increment the number of islands by 1.
11. We return the number of islands. """