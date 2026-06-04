# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None
        start = None
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if newhead is None:
                if list1.val < list2.val:
                    start = list1
                    newhead = list1
                    list1 = list1.next
                elif list1.val > list2.val:
                    start = list2
                    newhead = list2
                    list2 = list2.next
                else:
                    start = list1
                    newhead = list1
                    list1 = list1.next
            else:
                if list1.val < list2.val:
                    newhead.next = list1
                    list1 = list1.next
                    newhead = newhead.next
                elif list1.val > list2.val:
                    newhead.next = list2
                    list2 = list2.next
                    newhead = newhead.next
                else:
                    newhead.next = list1
                    newhead = newhead.next
                    list1 = list1.next
        if list1:
            newhead.next = list1
        elif list2:
            newhead.next = list2
        return start

