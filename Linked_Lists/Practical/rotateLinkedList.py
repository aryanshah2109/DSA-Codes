# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        ## TC = O(n) SC = O(1)

        if k == 0 or head is None:
            return head

        # Count number of elements:
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        
        if k % count == 0:
            return head

        k = k % count

        # Rotate
        tail = head
        prev = None
        index = 0
        while tail.next is not None:
            index += 1
            if index == count - k:
                prev = tail
            tail = tail.next

        newHead = prev.next
        tail.next = head
        prev.next = None
        
        return newHead
                        

