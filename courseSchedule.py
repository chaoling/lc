'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from collections import deque


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    '''
    This is a graph problem
    aka topological sort of graph
    Node: number of courses (V)
    edge: number of indegree(E)
    so total complexity: V+E
    (V1)<--(V2)<--(V3)
    ^
    |
    |
    (V0)
    so the prereq data structure needs to be converted to graph reps aka each node with its neighbors
    '''

    gp = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a,b in prerequisites:
        # pre contains a pair [ai, bi]
        gp[b].append(a) #edge from b->a #aka list of course that use this course as prereqs
        indegree[a] += 1
    
    #now we start with node of indgree 0 and traverse the graph and do a topological sort, aka a priority queue with order of indegrees in asending order
    #because we want to take the course with 0 prereqs first, after taken these pres, we reduce the indegree by 1 and keep sorting until all nodes are sorted.
    #so do a BFS, need a deque to sort nodes with least amount of indegrees in front of the queue
    dq = deque()
    for course in range(numCourses):
        if indegree[course] == 0:
            dq.append(course) #add courses that has zero prereqs first in the queue

    # Count how many courses we can visit in topological order
    visited = 0
    # Process node in queue
    while dq:
        current = dq.popleft()
        visited += 1

        # For each deps/neighbor, reduce its in-degree by 1
        for neighbor in gp[current]:
            indegree[neighbor] -= 1 #all course that has this current course as prereqs now can cross it out since it is visited or taken.
            # add it to queue if the neighbor now has 0 in-degree
            if indegree[neighbor] == 0:
                dq.append(neighbor)

    # If we've visited all courses in topological order, return True
    return visited == numCourses
    


def canFinishDFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    '''
    we can use DFS to detect whether ther's a cycle in the graph
    if a cycle exists, you cannot complete all courses
    during dfs, mark each node with a visitation state:
    0 - Not visited yet
    1 - Visiting (currently in the recursion stack)
    2 - visited (fully explored, no cycle found on this path)
    note: may have limit by the recursive stack size!!!
    '''
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[b].append(a)  #b->a

    visit_status = [0] * numCourses

    def dfs(course):
        # if we're visiting this node again before finishing, it means a cycle!
        if visit_status[course] == 1:
            return False
        # no need to visit if already fully visited
        if visit_status[course] == 2:
            return True
        
        # Mark current node as visiting or 1
        visit_status[course] = 1

        # check all neighbors
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False #cycle detected in the chain
        
        # Mark current node as fully visited (no cycle found in its path)
        visit_status[course] = 2
        return True
    
    #run dfs on each course:
    for c in range(numCourses):
        if visit_status[c] == 0:
            if not dfs(c):
                return False
    
    return True