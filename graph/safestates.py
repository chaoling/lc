'''
802. Find Eventual Safe States

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
'''
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        convert this problem to cycle detection: safte nodes are the nodes that has no cycles if do dfs from that node
        or node that is e terminal node
        O(N+E)
        '''
        n = len(graph)
        safe = [0] * n #0: unvisited, 1: safe, -1:unsafe

        def dfs(node: int) -> bool:
            # test if start from node i, the graph leads to a cycle in the dfs fashion:
            # True: The current node is safe, i.e., all paths starting from this node eventually lead to terminal nodes (no cycles).
            # False: The current node is unsafe, i.e., at least one path from this node leads to a cycle.
            if safe[node] != 0: 
                return safe[node] == 1 # 1 is safe, -1 is unsafe, since we encountered a cycle.
            safe[node] = -1 # Mark as visiting
            for nei in graph[node]:
                if not dfs(nei): # if any neighbor is unsafe
                    return False # current node is also unsafe
            safe[node] = 1 #Mark as safe since e made it through the loop, memoize this fact
            return True
        
        return [i for i in range(n) if dfs(i)]
