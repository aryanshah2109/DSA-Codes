# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverse(self, head):
        prev = None
        temp = head
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        head = prev
        return head

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ## TC = O(2N) SC = O(1)

        # Find out the middle of the linkedlist
        # For even number of elements, first element out of the 2 middle elements
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        # reverse elements from slow.next to end
        newHead = self.reverse(slow.next)

        # compare elements from start -> slow and newHead to last and if all equal, return True
        first = head
        second = newHead
        palindrome = True

        while second is not None:
            if first.val != second.val:
                palindrome = False
                break
            first = first.next
            second = second.next

        # Re reverse reversed linked list
        slow.next = self.reverse(newHead)

        return palindrome


