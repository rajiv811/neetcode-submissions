# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getMax(node,curr_max):
            if not node:
                return 0
            if node.val >= curr_max:
                return 1 + getMax(node.left,node.val) + getMax(node.right,node.val)
            return getMax(node.left,curr_max) + getMax(node.right,curr_max)
            
        return getMax(root,root.val)