'''
1466. Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 
Constraints:

2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
'''
from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        treat the graph as undirected, do dfs, if edges are forward dir, reverse it
        '''
        visited = set()
        directed_edges = set()
        graph = [[] for _ in range(n)]
        # Convert edge to adjacent list to represent graph (treat it as non-directional)
        for edge in connections:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
            directed_edges.add((a,b))

        def dfs(node: int) -> int:
            if node not in visited:
                visited.add(node)
            changes = 0
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                if (node, neighbor) in directed_edges:
                    changes += 1
                changes += dfs(neighbor)
            return changes
        
        return dfs(0)
if __name__ == "__main__":
    sol = Solution()
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(sol.minReorder(n, connections))  # Output: 3
    n2 = 5
    connections2 = [[1,0],[1,2],[3,2],[3,4]]
    print(sol.minReorder(n2, connections2))  # Output: 2
    n3 = 3
    connections3 = [[1,0],[2,0]]
    print(sol.minReorder(n3, connections3))  # Output: 0