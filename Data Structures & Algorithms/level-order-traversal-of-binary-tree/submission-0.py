# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [[root,0]]

        while stack:
            node,level = stack.pop()
            res.append([])
            res[level].append(node.val)

            if node.right:
                stack.append([node.right,level+1])
            if node.left:
                stack.append([node.left,level+1])
        
        final_res = []
        for l in res:
            if l != []:
                final_res.append(l)
        return final_res

        