# Given an m x n 2D binary grid grid 
# which represents a map of '1's (land) and '0's (water), 
# return the number of islands.
# An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
###############################################################
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
###############################################################

# approach 1(BFS)
# reference: https://www.youtube.com/watch?v=pV2kpPD66nE
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
def numIslands(grid):
    import collections
    if not grid: return 0
    island, row, col, vset = 0, len(grid), len(grid[0]), set()
    
    def bfs(r,c):
        q = collections.deque()
        vset.add((r,c))
        q.append((r,c))
        while q: 
            rr, cc = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = rr+dr, cc+dc
                if(r in range(row) and
                    c in range(col) and 
                    grid[r][c] == "1" and
                    (r,c) not in vset):
                    q.append((r,c))
                    vset.add((r,c))

    for r in range(row):
        for c in range(col):
            if (grid[r][c] == "1" and 
                (r,c) not in vset):
                bfs(r,c)
                island += 1
    return island

## Driver code
if __name__=='__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    print(numIslands(grid))