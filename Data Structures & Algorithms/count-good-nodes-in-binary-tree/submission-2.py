# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS / BFS search
        each time you visit a node, store largest value seen.
        If x.val > largest_seen, increment good nodes
        """
        def search(root,largest_val):
            count = 0
            q = deque([(root,largest_val)])
            while q:
                node,largest = q.popleft()
                if node.val >= largest:
                    count += 1
                    largest = node.val
                if node.left:
                    q.append((node.left,largest))
                if node.right:
                    q.append((node.right,largest))
            return count
        return search(root,root.val)
