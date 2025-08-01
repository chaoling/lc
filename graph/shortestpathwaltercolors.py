'''
1129. Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
'''
from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        '''
        shortest path -> BFS
        '''
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        # convert edges to graph adj list
        for edge in redEdges:
            a, b = edge[0], edge[1]
            red_adj[a].append(b)

        for edge in blueEdges:
            u, v = edge[0], edge[1]
            blue_adj[u].append(v)
        

        ans = [-1] * n
        q = deque([(0,'r'),(0,'b')])
        level = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if (node, color) in visited:
                    continue
                visited.add((node, color))
                if ans[node] == -1:
                    ans[node] = level
                next_adj = blue_adj if color == 'r' else red_adj
                next_color = 'b' if color == 'r' else 'r'
                for nei in next_adj[node]:
                        q.append((nei, next_color))
            level += 1
        return ans