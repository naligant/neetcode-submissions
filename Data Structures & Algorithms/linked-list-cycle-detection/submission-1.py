# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        newhead = head
        visited = set()
        while newhead:
            if newhead not in visited:
                visited.add(newhead)
            else:
                return True
            newhead = newhead.next
        return False