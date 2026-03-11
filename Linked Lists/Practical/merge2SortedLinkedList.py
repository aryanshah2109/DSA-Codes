# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp1 = list1
        temp2 = list2

        temp3 = ListNode()
        dummyNode = temp3
        

        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                newNode = ListNode(temp1.val)
                temp3.next = newNode
                temp3 = newNode
                temp1 = temp1.next
            else:
                newNode = ListNode(temp2.val)
                temp3.next = newNode
                temp3 = newNode
                temp2 = temp2.next
        
        # if 1st list is over
        while temp2 is not None:
            newNode = ListNode(temp2.val)
            temp3.next = newNode
            temp3 = newNode
            temp2 = temp2.next
        
        # if 2nd list is over
        while temp1 is not None:
            newNode = ListNode(temp1.val)
            temp3.next = newNode
            temp3 = newNode
            temp1 = temp1.next
        
        return dummyNode.next