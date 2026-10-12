class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        rows, cols = len(grid), len(grid[0])
        res = 0 
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0 
            if (row,col) in visited:
                return 0
            visited.add((row, col))
            size = 1
            for d in directions:
                size += dfs(row + d[0] ,col+d[1])
            return size
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for row in range(rows):
            for col in range(cols):
            
                res = max(res, dfs(row, col))

        return res
            