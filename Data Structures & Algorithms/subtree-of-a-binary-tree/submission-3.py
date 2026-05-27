# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case - If we exhaust through entire tree, and get to Null value,
        #then subtree does not exist in this particular path
        if not root:
            return False
        #Algo
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def isSameTree(self,root,subRoot):
        #base case
        if not root and not subRoot:
            return True
        #Algo
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)
        else:
            return False