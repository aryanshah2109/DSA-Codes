# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Brute
        # TC = O(n) SC = O(1)
        # if head is None or (head.next is None and n == 1):
        #     return None
        
        # count = 0
        # temp = head

        # while temp is not None:
        #     count += 1
        #     temp = temp.next
            
        # if n == count:  # Head is to be deleted
        #     return head.next

        # prev_index = count - n 
        # current_index = 0
        # temp = head
        # while temp is not None:
        #     current_index += 1
        #     if current_index == prev_index:
        #         temp.next = temp.next.next
        #         break
        #     temp = temp.next
        # return head



        # Optimal
        # TC = O(n) SC = O(1)

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast is None: # Have to delete head
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head


