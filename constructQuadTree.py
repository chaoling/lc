'''
427. Construct Quad Tree
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6
'''
# Definition for a QuadTree node.
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
         At any level, if the current subgrid is uniform (all values same),
        it becomes a leaf node. Otherwise, recursively subdivide into 4 quadrants.
        '''
        def isUniform(r1,c1,r2,c2) -> bool:
            #given a sub_region topleft->bottomright, return if it is uniform
            sample = grid[r1][c1]
            for row in range(r1,r2+1):
                for col in range(c1,c2+1):
                    if grid[row][col] != sample:
                        return False
            else:
                return True

        def build(r1,c1,r2,c2):
            # n == 2^x where 0<= x <= 6
            if r1 > r2 or c1 > c2:
                return None
            if isUniform(r1,c1,r2,c2):
                curr = Node(grid[r1][c1]==1,True,None, None, None, None)
            else:
                # Not uniform, so split into 4 quadrants and recurse
                midRow = (r1 + r2) // 2
                midCol = (c1 + c2) // 2
                curr = Node(True,False,None, None, None, None)
                curr.topLeft = build(r1,c1,midRow,midCol)
                curr.topRight = build(r1,midCol+1,midRow,c2)
                curr.bottomLeft = build(midRow+1,c1,r2,midCol)
                curr.bottomRight = build(midRow+1,midCol+1,r2,c2)
            return curr

        n = len(grid)
        return build(0,0,n-1,n-1)

if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    sol = Solution()
    root = sol.construct(grid)
    
    # Function to print the tree in pre-order for testing
    def print_tree(node):
        if not node:
            return
        print(f'Node(val={node.val}, isLeaf={node.isLeaf})')
        print_tree(node.topLeft)
        print_tree(node.topRight)
        print_tree(node.bottomLeft)
        print_tree(node.bottomRight)

    print_tree(root)  # Output: structure of the QuadTree