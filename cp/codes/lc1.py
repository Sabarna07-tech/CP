from typing import List

class Solution:
    def countRowFlips(self, row: List[int]) -> int:
        n = len(row)
        flips = 0
        for j in range(n // 2):
            if row[j] != row[n - 1 - j]:
                flips += 1
        return flips

    def countColumnFlips(self, grid: List[List[int]], col: int) -> int:
        m = len(grid)
        flips = 0
        for i in range(m // 2):
            if grid[i][col] != grid[m - 1 - i][col]:
                flips += 1
        return flips

    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        rowFlips = 0
        for i in range(m):
            rowFlips += self.countRowFlips(grid[i])

        colFlips = 0
        for j in range(n):
            colFlips += self.countColumnFlips(grid, j)

        return min(rowFlips, colFlips)