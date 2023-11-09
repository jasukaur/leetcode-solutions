# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1

        curr = h1 = None

        
        if list1.val <= list2.val:
            curr = list1
            list1 = list1.next
        else:
            curr = list2
            list2 = list2.next
        h1 = curr
        
        while list1 and list2:
            print(list1.val, list2.val)
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return h1



        