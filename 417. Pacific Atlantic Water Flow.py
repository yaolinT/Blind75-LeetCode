# There is an m x n rectangular island 
# that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, 
# and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. 
# You are given an m x n integer matrix heights 
# where heights[r][c] represents the height above sea level 
# of the cell at coordinate (r, c).
# The island receives a lot of rain, 
# and the rain water can flow to neighboring cells directly 
# north, south, east, and west 
# if the neighboring cell's height 
# is less than or equal to the current cell's height. 
# Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result 
# where result[i] = [ri, ci] denotes 
# that rain water can flow from cell (ri, ci) 
# to both the Pacific and Atlantic oceans.
###############################################################
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
###############################################################

# approach 1(DFS, O(n*m))
# reference: https://www.youtube.com/watch?v=s-VkcjHqkGI
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
def pacificAtlantic(heights):
    row, col, po, ao = len(heights), len(heights[0]), set(), set()
    temp = []
    
    def dfs(r, c, vset, prevh):
        if ((r,c) in vset or
            r < 0 or
            c < 0 or
            r == row or
            c == col or
            heights[r][c] < prevh):
            return
        vset.add((r,c))
        dfs(r+1, c  , vset, heights[r][c])
        dfs(r-1, c  , vset, heights[r][c])
        dfs(r  , c+1, vset, heights[r][c])
        dfs(r  , c-1, vset, heights[r][c])
        
    for c in range(col):
        dfs(0, c, po, heights[0][c])
        dfs(row-1, c, ao, heights[row-1][c])
    for r in range(row):
        dfs(r, 0, po, heights[r][0])
        dfs(r, col-1, ao, heights[r][col-1])
    for r in range(row):
        for c in range(col):
            if (r,c) in po and (r,c) in ao:
                temp.append([r,c])
    return temp

## Driver code
if __name__=='__main__':
	heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
	print(pacificAtlantic(heights))
