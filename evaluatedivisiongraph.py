'''
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''
from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        How come this can be modeled as the graph problem? A direct weighted graph with weight a->b equals to a/b aka the values[i] 
        and b->a = b/a aka the 1/values[i] ?
        then the queries simply becomes if there is a route from a->c : a->b->c : a/b * b/c
        or b->a = b/a = 1/(a/b) = 1/values[i]
        Question: how to represent such a graph? -> as dictionary of dict
        Suppose equations = [["a", "b"], ["b", "c"]], values = [2.0, 3.0]
        graph = {
            "a": {"b": 2.0},
            "b": {"a": 0.5, "c": 3.0},
            "c": {"b": 1/3.0}
        }
        '''
        def dfs(graph, start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue
                product = dfs(graph, neighbor, end, visited)
                if product != -1.0:
                    return val * product
            return -1.0

        from collections import defaultdict
        ans = []
        graph = defaultdict(dict)

        for (u,v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1/val
      
        for (u,v) in queries:
            ans.append(dfs(graph,u,v,set()))
        
        return ans

if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    sol = Solution()
    print(sol.calcEquation(equations, values, queries))  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]