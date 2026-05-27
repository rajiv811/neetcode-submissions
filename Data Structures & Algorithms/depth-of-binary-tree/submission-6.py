class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        queue = deque([[root,1]])
        max_depth = 0
        while queue:
            node,depth = queue.popleft()
            if not node.left and not node.right:
                max_depth = max(max_depth,depth)
            if node.left:
                queue.append([node.left,depth+1])
            if node.right:
                queue.append([node.right,depth+1])
        return max_depth
