class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            grid[r][c] = 'W'  # Mark the cell as visited
            dfs(r - 1, c)  # Explore up
            dfs(r + 1, c)  # Explore down
            dfs(r, c - 1)  # Explore left
            dfs(r, c + 1)  # Explore right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    count += 1
                    dfs(r, c)  # Start DFS for each new island
        
        return count
