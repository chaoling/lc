'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 
Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''
# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index = idx_map[root_val]
            
            # build right subtree first because we are consuming postorder from the end
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
        return helper(0, len(inorder) - 1)
# The above implementation uses a hashmap to store the indices of inorder elements, which allows us to find the index in O(1) time.
# This significantly improves the time complexity to O(n) for the overall function, where n is the number of nodes in the tree.
# The space complexity remains O(n) for the recursion stack and the output tree structure.
    def buildTree_initial(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        from postorder: we get root-> postorder[-1] => 3
        now we can locate this in inorder index: i = 1, aka inorder[1] => 3
        postorder => [None, None, 9, | 15,7,20]
        postorder => [None, None | 15,7]
        left: 15, right half: 7 
        left half of the tree: inorder[:i] --> [None, 9, None]
        right half of the tree: inorder[i+1:] --> [15,20,7]
        output: in level order, and if no leaf, using None instead.
        [3, 9, 20, None, None, 15, 7, _,_,_,_,_,_,_,_]
        '''
        def bTree(inorder, postorder):
            n = len(postorder)
            #since it is a binary tree, the output length is always ==> 2^m where m = int(log2(n))
            if n == 0:
                return 
            rval = postorder[-1]
            root = TreeNode(rval) #root is always the last element of postorder list
            # next step is to find out the left and right half of the tree
            # 1st seperate the left and right half of the tree with their own inorder and corresponding postorder list 
            root_index = inorder.index(rval)
            inorder_left, inorder_right = inorder[:root_index], inorder[root_index+1:]
            postorder_left, postorder_right = postorder[:root_index], postorder[root_index:-1]
            root.left = bTree(inorder_left, postorder_left)
            root.right = bTree(inorder_right, postorder_right)
            return root
        return bTree(inorder, postorder)
        # Time Complexity: O(n^2) in the worst case, O(n) in the best case
        # Space Complexity: O(n) for the recursion stack and the output tree structure
        # Note: The index method in Python is O(n), which makes the overall complexity O(n^2) in the worst case.
        # However, if we use a hashmap to store indices of inorder elements, we can reduce it to O(n).
        # This implementation is straightforward and easy to understand, but not optimal for large trees.
        # Note: The above implementation is not optimal for large trees due to the O(n) index search in inorder.
        # To optimize, we can use a hashmap to store the indices of inorder elements.
        # This will reduce the time complexity to O(n) for the overall function.
    
def print_tree(node):
    # Function to print the tree in level order
    if not node:
        return "None"
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("None")
    return result
    
if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    tree = sol.buildTree(inorder, postorder)
    # The tree can be printed or traversed to verify correctness. write a function to print the tree in level order
    print(print_tree(tree))  # Output should be the level order traversal of the tree
