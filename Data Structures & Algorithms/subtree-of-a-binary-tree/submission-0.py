# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if self.isSameTree(node,subRoot):
                return True
        return False

    def isSameTree(self,root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.isSameTree(root.left,subroot.left) and self.isSameTree(root.right,subroot.right)
        else:
            return False
