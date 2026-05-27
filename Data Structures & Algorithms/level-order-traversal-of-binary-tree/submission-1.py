# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
inorder - Left -> Root -> right
pre - Root -> Left -> Right
post -  Left -> Right -> Root
level - visits all nodes in a level before moving on
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[]]
        q = deque([(root,0)])
        while q:
            node,level = q.popleft()
            print("res",len(res))
            print("level",level)
            if len(res)-1 < level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        return res
