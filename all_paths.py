'''
797. All Paths From Source to Target
Solved
Medium
Topics
Companies
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
'''
from typing import List
from collections import deque


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
        '''
        DAG: fixed start (0) and end (n-1) node
        check all pathes from 0, save the path if it can reach n-1
        using dfs with backtracking
        '''
        output = []
        def dfs(current_node: int, current_path: list[int], graph: List[List[int]]):
            current_path.append(current_node)
            if current_node == len(graph) - 1:
                #print(f'find one path! {current_path=}')
                output.append(current_path[:]) #need a copy, otherwise would be modified by the pop, reference vs copy
                return
            
            for node in graph[current_node]:
                #add it to current path
                dfs(node, current_path, graph)
                #print(f"{node=}, {current_path=}")
                current_path.pop()
                #print(f"after backtracking... {current_path=}")

        dfs(0, [], graph)
        return output

if __name__=="__main__":
     graph = [[4,3,1],[3,2,4],[3],[4],[]]
     res = allPathsSourceTarget(graph)
     print("================== Solution is.... ===========================")
     print(res)