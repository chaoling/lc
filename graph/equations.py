'''
990. Satisfiability of Equality Equations

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.


Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 

Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
'''

import string
from pyparsing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        Build an undirected graph with only "==" edges and find its connected components.
        '''
        from collections import defaultdict
        import string
        graph = defaultdict(set)
        # or use graph = [[] for _ in range(26)]
        # convert 'a'..'z' into indices with ord(c) - ord('a')
        for eq in equations:
            #only look at ==:
            if eq[1] == '=':
                a,b = eq[0], eq[3]
                graph[a].add(b)
                graph[b].add(a)
        
        #now find connected components:
        def dfs(node, id):
            visited.add(node)
            component_id[node] = id
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, id)

        visited = set()
        component_id = {}
        cid = 0
        for v in list(string.ascii_lowercase):
            if v not in visited:
                dfs(v, cid)
                cid += 1

        
        
        #now look for contradictions :
        for eq in equations:
            if eq[1] == '!':
                a,b = eq[0],eq[3]
                if a == b or component_id[a] == component_id[b]:
                    return False
        return True


    def equationsPossibleUnionFind(self, equations: List[str]) -> bool:
        '''
        Union-Find solution
        '''
        parent = list(range(26))
        size = [1] * 26

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression (halving)
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry: 
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        def idx(c):
            return ord(c) - ord('a')

        # 1) Unite all "==" pairs
        for eq in equations:
            if eq[1] == '=':  # "x==y"
                union(idx(eq[0]), idx(eq[3]))

        # 2) Check all "!=" pairs for contradiction
        for eq in equations:
            if eq[1] == '!':  # "x!=y"
                x, y = idx(eq[0]), idx(eq[3])
                if find(x) == find(y):  # same set => contradiction
                    return False

        return True