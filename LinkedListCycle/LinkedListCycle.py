# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False
        
# Idea, use a fast and slow pointer.
# [ 3, 2, 0, -4 ]
# OK so what the hell am I supposed to do. Let's think about that.
# fast, slow = [3], [0]
# So we are going to progress the two pointers at the same time.
# while fast is not pointed to the end and fast.next exists
# 1st: [3] [0] -> [2] and [2]
# 2nd: 