from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Optimal - Slow Fast Approach

        # Detect if any cycle exists 
        slow = head
        fast = head
        hasCycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        # Detect starting node
        if hasCycle :
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        
        # No cycle exists
        return None
