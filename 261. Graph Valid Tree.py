# Given n nodes labeled from 0 to n-1 
# and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.
# (Sample I/O)

# Note: 
# you can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0,1] is the same as [1,0] 
# and thus will not appear together in edges.
###############################################################
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true

# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
###############################################################

# approach 1(DFS, Topological sort)
# reference: https://www.youtube.com/watch?v=bXsUuownnoQ
# def validTree(self, n: int, edges: List[List[int]]) -> bool:
def validTree(n, edges):
    if not n:
        return True
    adj = {i:[] for i in range(n)}
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    vset = set()
    def dfs(i, p):
        if i in vset:
            return False
        vset.add(i)
        for j in adj[i]:
            if j == p:
                continue
            if not dfs(j, i):
                return False
        return True
    return dfs(0, -1) and n == len(vset)

## Driver code
if __name__=='__main__':
    n, edges = 5, [[0,1], [0,2], [0,3], [1,4]]
    print(validTree(n, edges))