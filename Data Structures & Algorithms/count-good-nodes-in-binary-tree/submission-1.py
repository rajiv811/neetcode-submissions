# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root will alwats be a good node
        # root is minimum value, if less do not consider
        # track minimum variable
        if not root:
            return 0
        
        def dfs(root):
            res = []
            stack = [[root,root.val]]

            while stack:
                node,max_val = stack.pop()
                if node.val >= max_val:
                    res.append(node.val)
                    max_val = node.val
                if node.left:
                    stack.append([node.left,max_val])
                if node.right:
                    stack.append([node.right,max_val])   
            return len(res)             

        return dfs(root)
            

        