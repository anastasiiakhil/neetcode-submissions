# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr_node = head

        while curr_node:
            tmp = curr_node.next       # old pointer
            curr_node.next = prev      # upd/reversed pointer
            prev = curr_node           # upd prev pointer
            curr_node = tmp            # tmp saved original curr mode

        return prev
