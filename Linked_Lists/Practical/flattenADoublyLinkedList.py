from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        while curr is not None:
        
            # If child exists
            if curr.child is not None:
            
                # Store next node address
                next_ptr = curr.next
        
                # Take entire child and store in next pointer of current node
                curr.next = self.flatten(curr.child)

                # make reverse connection of child to parent
                curr.next.prev = curr

                # make sure the child pointer becomes null
                curr.child = None

                # Find out the tail of the child
                while curr.next is not None:
                    curr = curr.next

                # Connect resultant child linkedlist with original next pointer
                if next_ptr is not None:
                    curr.next = next_ptr
                    next_ptr.prev = curr

            # If child doesnt exist
            curr = curr.next

        return head
