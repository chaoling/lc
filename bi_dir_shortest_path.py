from collections import deque
from typing import List

def bidirectional_shortest_path(graph: List[List[int]], start: int, target: int) -> List[int]:
    # For a directed graph, construct the reverse graph.
    # For an undirected graph, reverse_graph is the same as graph.
    n = len(graph)
    reverse_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)
    
    # Initialize queues for both directions
    forward_queue = deque([start])
    backward_queue = deque([target])
    
    # Dictionaries to track parents in both searches (for path reconstruction)
    forward_parents = {start: None}
    backward_parents = {target: None}
    
    # Variable to store the meeting point
    meeting_node = None
    
    # Helper function to expand one level in one direction.
    def expand_level(queue: deque, parents: dict, other_parents: dict, graph_direction: List[List[int]]):
        nonlocal meeting_node
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph_direction[current]:
                if neighbor not in parents:
                    parents[neighbor] = current
                    queue.append(neighbor)
                    # Check if this node has been seen from the other direction.
                    if neighbor in other_parents:
                        meeting_node = neighbor
                        return True
        return False
    
    # Run BFS from both ends until a meeting point is found.
    while forward_queue and backward_queue and meeting_node is None:
        # Expand the search from the side with fewer nodes.
        if len(forward_queue) <= len(backward_queue):
            if expand_level(forward_queue, forward_parents, backward_parents, graph):
                break
        else:
            if expand_level(backward_queue, backward_parents, forward_parents, reverse_graph):
                break
    
    if meeting_node is None:
        # No path exists between start and target.
        return []
    
    # Reconstruct the path from start to meeting_node.
    path_forward = []
    node = meeting_node
    while node is not None:
        path_forward.append(node)
        node = forward_parents[node]
    path_forward.reverse()  # Now it goes from start to meeting_node.
    
    # Reconstruct the path from meeting_node to target.
    path_backward = []
    node = backward_parents[meeting_node]
    while node is not None:
        path_backward.append(node)
        node = backward_parents[node]
    
    # Combine the two parts to form the full path.
    return path_forward + path_backward


def shortestPathBFS(graph: list[list[int]], start: int, target: int) -> list[int]:
    # Initialize the queue with the starting path
    queue = deque([[start]])

    visited = {start}

    while queue:
        path = queue.popleft()
        curr_node = path[-1]
        #if we reached the target, return the path, is it already the shortest
        if curr_node == target:
            return path
        #otherwise, extend the path to all unvisited neighbors
        for node in graph[curr_node]:
            if node not in visited:
                visited.add(node)
                queue.append(path+[node])

    #if target is not reachable, return any empty list or None
    return []

if __name__ == "__main__":
    # Example graph: change this to your own test case.
    # This example is for an undirected graph; if directed, ensure reverse_graph is computed.
    graph = [
        [1, 2],    # Neighbors of node 0
        [0, 3, 4], # Neighbors of node 1
        [0, 4],    # Neighbors of node 2
        [1, 5],    # Neighbors of node 3
        [1, 2, 5], # Neighbors of node 4
        [3, 4]     # Neighbors of node 5
    ]
    start, target = 0, 5
    shortest_path = bidirectional_shortest_path(graph, start, target)
    print("Shortest path from {} to {} is: {}".format(start, target, shortest_path))
    verify_path = shortestPathBFS(graph, start, target)
    print("Shortest path from {} to {} is: {}".format(start, target, verify_path))


