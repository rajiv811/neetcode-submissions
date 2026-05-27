# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None,head

        while curr:
            tmp = curr.next # 1->2->3->None
            curr.next = prev # 0->None
            prev = curr #0->None
            curr = tmp
        return prev



        