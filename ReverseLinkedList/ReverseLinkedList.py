# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        extra = None
        current = head

        while current != None:
            head = current.next
            current.next = extra
            extra = current
            current = head
        
        return extra

"""
initial: NULL [1] -> [2] -> [3] -> [4] -> [5] -> NULL
         ^     ^
         Extra Head
               Current
final: NULL <- [1] <- [2] <- [3] <- [4] <- [5]
                                            ^
                                            Head
how do I do this?

first set head to point to cur.next until NULL

3 pointers to update and track
extra: NULL
current.next: [2]
head: [2]
current: [1]

1. Head to current.next
2. current.next to extra
3. extra to current
4. current to head Loop until current is None

"""
        