from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        oldHead = head
        newHead = Node(oldHead.val)
        mappings = {}
        mappings[head] = newHead

        # Step 1: Create normal linked list
        oldTemp = oldHead.next
        newTemp = newHead
        while oldTemp is not None:
            newNode = Node(oldTemp.val)
            mappings[oldTemp] = newNode
            newTemp.next = newNode
            oldTemp = oldTemp.next
            newTemp = newTemp.next
            
        # Step 2: Copy random pointers
        oldTemp = oldHead
        newTemp = newHead
        while oldTemp is not None:
            newTemp.random = mappings.get(oldTemp.random)
            oldTemp = oldTemp.next
            newTemp = newTemp.next
        
        return newHead

        