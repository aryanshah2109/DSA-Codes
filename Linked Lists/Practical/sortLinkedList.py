# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def merge2Lists(self, left, right):
        tail = ListNode()
        dummyNode = tail


        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        else:
            tail.next = right

        return dummyNode.next


    def sort(self, head):
        # Step 0: Validate head
        # If zero or single element:
        if head is None or head.next is None:
            return head


        # Step 1: Find middle element of linked list
        middle = self.findMiddle(head)

        # Step 2: Merge sort 
        leftListHead = head
        rightListHead = middle.next
        
        middle.next = None

        leftListHead = self.sort(leftListHead)
        rightListHead = self.sort(rightListHead)

        mergedListHead = self.merge2Lists(leftListHead, rightListHead)

        return mergedListHead


    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        ## Brute Force
        ## TC = O(n + nlogn + n) SC = O(n)

        ## 1) Copy the linked list elements into an array
        ## 2) Sort the array
        ## 3) Modify given linked list with sorted array elements
        ## 4) Return the head of the linked list

        ## Optimal -> Merge Sort the linked list

        return self.sort(head)
