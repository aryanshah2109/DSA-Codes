from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while count < k:
            # Nodes less than k left, then do not reverse
            if temp is None:
                return head
            count += 1
            temp = temp.next
        
        # Recursively reverse nodes from k+1 to last node
        previous_node = self.reverseKGroup(temp, k)

        # Reverse from current node to kth node
        temp = head
        count = 0
    
        while count < k:
            next_ptr = temp.next
            temp.next = previous_node
            previous_node = temp
            temp = next_ptr
            count += 1
        
        return previous_node
