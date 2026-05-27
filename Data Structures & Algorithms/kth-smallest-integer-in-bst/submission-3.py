# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        return kth smallest value in tree
        if k = 1, return lowest number
        if k = n, return highest number
        Naive solution - flatten tree, sort, find k value
        - o(nlogn) solution

        Advanced solution - iterate through bst in order, iterate n-k times
        until you find solution
        """

        q = [root]
        l = []
        while q:
            node = q.pop()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        l.sort()
        
        if k == 1:
            return l[0]
        if k == len(l):
            return l.pop()
        for val in l:
            k-= 1
            if k == 0:
                return val

            



