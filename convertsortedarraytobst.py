'''
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Divide and Conquer:
        for each sublist, find the middle node as root, then do the left subtree and right subtree
        '''
        def helper(left, right)-> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(val=nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root

        return helper(0, len(nums)-1)
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    bst_root = sol.sortedArrayToBST(nums)
    
    # Function to print the tree in pre-order for testing
    def print_tree(node):
        if not node:
            return
        print(node.val, end=' ')
        print_tree(node.left)
        print_tree(node.right)

    print_tree(bst_root)  # Output: 0 -10 -3 5 9
# This will print the pre-order traversal of the BST created from the sorted array.
# The output will show the structure of the BST.
# The expected output is a balanced BST with 0 as the root, -10 and -3 as the left subtree, and 5 and 9 as the right subtree.
# The output will be in pre-order traversal format.
# The output will be: 0 -10 -3 5 9