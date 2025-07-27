'''
1192. Critical Connections in a Network

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.


Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
'''
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.time = 0

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Use Depth-First Search (DFS) to explore the graph while keeping track of:
        Discovery Time: When a node is first visited.
        Low Link Value: The earliest (lowest) discovery time reachable from that node — either  directly or through its descendants via back edges.
        '''
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = [-1] * n #visit time of nodes
        low = [-1] * n #earliest visited nodes
        res = []

        def dfs(u, parent):
            visit[u] = low[u] = self.time
            self.time += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if visit[v] == -1:
                    dfs(v,u)
                    low[u] = min(low[u], low[v])
                    if low[v] > visit[u]:
                        res.append([u,v])
                else:
                    low[u] = min(low[u], visit[v])
        for i in range(n):
            if visit[i] == -1:
                dfs(i, -1)
        
        return res