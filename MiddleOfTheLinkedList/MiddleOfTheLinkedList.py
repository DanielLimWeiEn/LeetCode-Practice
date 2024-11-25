# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

"""
[1] -> [2] -> [3] -> [4] -> [5] -> [6]

slow = [1] -> [2] -> [3] -> [4]
fast = [1] -> [3] -> [5] -> None

while fast and fast.next:
    

[1] -> [2] -> [3] -> [4] -> [5]

slow = [1] -> [2] -> [3]
fast = [1] -> [3] -> [5]




"""
