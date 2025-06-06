'''
173. Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = []
        self._left_most_inorder(root) #populate the internal ds
    
    def _left_most_inorder(self, node: Optional[TreeNode]):
        while node:
            self.iter.append(node)
            node = node.left

    def next(self) -> int:
        top = self.iter.pop()
        if top.right:
            self._left_most_inorder(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.iter) > 0
    
    
    '''
    def __init__(self, root: Optional[TreeNode]):

        self.current = root
        self.iter = []
        self._inorder(root) #populate the internal ds
        self.pos = 0
    
    def _inorder(self, node: Optional[TreeNode]):
        if node:
            self._inorder(node.left)
            self.iter.append(node.val)
            self._inorder(node.right)


    def next(self) -> int:
        val = self.iter[self.pos]
        self.pos += 1
        return val

    def hasNext(self) -> bool:
        return self.pos != len(self.iter)
    '''

# Your BSTIterator will be called like this:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()