# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        BST - left subtree < node , right subtree > node
        Python priority queue - Min heap by default
        """
        q = deque([root])
        pq = []
        while q:
            node = q.popleft()
            heapq.heappush(pq,-node.val)
            if len(pq) > k:
                heapq.heappop(pq)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        print(pq)
        return -pq[0]