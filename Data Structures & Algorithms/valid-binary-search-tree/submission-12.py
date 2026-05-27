# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,lower_limit,upper_limit):
            if not node:
                return True
            if not (lower_limit < node.val < upper_limit):
                return False
            return isValid(node.left, lower_limit, node.val) and isValid(node.right,node.val,upper_limit)

        return isValid(root,float("-inf"), float("inf"))