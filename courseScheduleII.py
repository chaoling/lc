from collections import deque
from typing import List


def find_course_schedule(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    '''
    Build the Graph:

    Use an adjacency list to represent the graph.

    Track the in-degree (number of prerequisites) for each course.

    Initialize the Queue:

    Add all courses with in-degree 0 to the queue — these have no prerequisites.

    Topological Sort (BFS):

    While the queue is not empty:

    Pop a course, add it to the result.

    Decrease the in-degree of its neighbors.

    If any neighbor’s in-degree becomes 0, add it to the queue.

    Check for Cycle:

    If the result contains all courses, return it.

    Otherwise, return an empty list (cycle detected).
    '''
    # build the adj list
    adj = [[] for _ in range(num_courses)]
    pre = [[] for _ in range(num_courses)]
    for item in prerequisites:
        course, prereqs = item[0], item[1]
        adj[prereqs].append(course)
        pre[course].append(prereqs)
    
    res = []
    # init the queue
    q =deque([i for i in range(num_courses) if len(pre[i] == 0)])
    order = []
    

    while q:
        current = q.popleft()
        order.append(current)
        for course in adj[current]:
            pre[course].remove(current) #reduce indegree by 1
            if not pre[course]:
                q.append(course) 
        
    return order if len(order) == num_courses else []

def sol2(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses

    for course, prereqs in prerequisites:
        adj[prereqs].append(course)
        indeg[course] += 1

    q = deque([i for i, d in enumerate(indeg) if d == 0])
    order = []
    while q:
        cur = q.popleft()
        order.append(cur)

        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    return order if len(order) == num_courses else []







    