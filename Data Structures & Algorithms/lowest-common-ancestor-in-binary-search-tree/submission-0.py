class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Case 1:
        # If p is a subtree of q, return q
        # Case 2:
        # If q is a subtree of p, return p
        # Case 3:
        # If p and q are not in the same subtree, return Node n such that
        # n.left subtree contains p, and n.right subtree contains q

        """
        What do we know about BSTs?
        root.left < root
        root.right > root

        if p > root, it is in right subtree
        if p < root, it is in left subtree
        same applies for q
        """
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

