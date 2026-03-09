# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # # Brute
        # # TC = O(n/2 + n/2 + n) ~ O(n)
        # # SC = O(n)
        # if head is None or head.next is None:
        #     return head

        # elements = []
        # temp = head
        # while temp is not None and temp.next is not None:
        #     elements.append(temp.val)
        #     temp = temp.next.next
        # if temp is not None:    # avoid skipping last element for odd lengthed Linkedlist
        #     elements.append(temp.val)
        
        
        # temp = head.next
        # while temp is not None and temp.next is not None:
        #     elements.append(temp.val)
        #     temp = temp.next.next
        # if temp is not None:    # avoid skipping last element for odd lengthed Linkedlist
        #     elements.append(temp.val)
        
        # temp = head
        # index = 0
        # while temp is not None:
        #     temp.val = elements[index]
        #     index += 1
        #     temp = temp.next
        # return head


        # Optimal
        # TC = O(n/2) ~ O(n) SC = O(1)
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even is not None and even.next is not None :
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head 