# Given n nodes labeled from 0 to n - 1 
# and a list of undirected edges (each edge is a pair of nodes), 
# write a function to find the number of connected components 
# in an undirected graph.
# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] 
# and thus will not appear together in edges.
###############################################################
#      0          3
#      |          |
#      1 --- 2    4
# Input: n = 5, and edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2

#      0           4
#      |           |
#      1 --- 2 --- 3
# Input: n = 5, and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# Output: 1
###############################################################

# approach 1(tree)
# reference: https://www.youtube.com/watch?v=8f1XPm4WOUc
def countComponents(n, edges):
    par = [i for i in range(n)]
    rank = [1] * n
    def find(a):
        temp = a
        while temp != par[temp]:
            par[temp] = par[par[temp]]
            temp = par[temp]
        return temp
    def union(a, b):
        A, B = find(a), find(b)
        if A == B:
            return 0
        if rank[B] > rank[A]:
            par[A] = B
            rank[B] += rank[A]
        else:
            par[B] = A
            rank[A] += rank[B]
        return 1
    for a, b in edges:
        n -= union(a, b)
    return n

## Driver code
if __name__=='__main__':
    n, edges = 5, [[0, 1], [1, 2], [3, 4]]
    print(countComponents(n, edges))