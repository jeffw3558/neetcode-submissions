class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid == None:
            return 0
        maximum = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
                     # interate thru grid
            if row < 0 or col <0 or row>=rows or col>=cols or (row,col) in visited:
                return
            if grid[row][col] == "0":
                return
            visited.add((row,col))
                
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                r, c = row+dr, col+dc
                dfs(r,c)

        for row in range(0,rows):
            for col in range(0,cols):
                if grid[row][col] =="1" and (row,col) not in visited:
                    dfs(row,col)
                    maximum+=1

        

        return maximum