'''
1376. Time Needed to Inform All Employees

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
 

Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
'''
from collections import deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        build a graph /tree such that the manager is on top and subordinates is its children
        the root node is the head of the company
        '''
        class EmployeeNode:
            def __init__(self, id, inform_time):
                self.id = id
                self.inform_time = inform_time
                self.subordinates = [] # list of treeNodes

        #build the company org tree from the manager table
        #first we build the dict /hashtable for easy look up employee nodes:
        nodes = {i: EmployeeNode(i, informTime[i]) for i in range(n)}
        root = None

        for emp_id, mgr_id in enumerate(manager):
            if mgr_id == -1:
                root = nodes[emp_id]
            else:
                nodes[mgr_id].subordinates.append(nodes[emp_id])
        
        #do level order traversal and compute the time taken along the way
        def dfs(node):
            if not node.subordinates:
                return 0
            max_sub_time = max(dfs(sub) for sub in node.subordinates)
            return node.inform_time + max_sub_time
        
        def bfs(node):
            max_time = 0
            queue = deque([(root,0)]) #(node, time_so_far)
            while queue:
                node, time = queue.popleft()
                max_time = max(max_time, time)
                for sub in node.subordinates:
                    queue.append((sub, time + node.inform_time))
            return max_time

        return bfs(root)



#######
from collections import defaultdict

def numOfMinutes(n, headID, manager, informTime):
    # Step 1: Build the org tree as dictionary
    tree = defaultdict(list)
    for emp, mgr in enumerate(manager):
        if mgr != -1:
            tree[mgr].append(emp)

    # Step 2: DFS to compute max time
    def dfs(emp_id):
        if not tree[emp_id]:
            return 0
        return informTime[emp_id] + max(dfs(sub) for sub in tree[emp_id])

    return dfs(headID)
