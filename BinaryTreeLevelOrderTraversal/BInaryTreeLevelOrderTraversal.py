# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        queue.append(( root, 1 ))
        res = []

        while queue:
            topElement, topElementLevel = queue.pop(0)

            curLevel = [topElement.val]

            if topElement.left:
                queue.append(( topElement.left, topElementLevel + 1 ))
            if topElement.right:
                queue.append(( topElement.right, topElementLevel + 1 ))
            
            while queue and queue[0][1] == topElementLevel:
                nextElement, nextElementLevel = queue.pop(0)
                curLevel.append(nextElement.val)
                if nextElement.left:
                    queue.append(( nextElement.left, nextElementLevel + 1 ))
                if nextElement.right:
                    queue.append(( nextElement.right, nextElementLevel + 1 ))
            
            res.append(curLevel)
        
        return res

"""

Ok, level order traversal.

Use a queue.

Maintain levels.

I can store each element in the queue as a tuple (element, level), just to make life simpler.

queue = [([3], 1)]

root = [3]

while queue:
    top = ([3], 1)

    curLevel = [[3]]
    
    queue.append((top.left if not null, top[1] + 1))
    queue.append((top.right if not null, top[1] + 1))

    while queue.peek()[1] is top[1]:
        dequeue and put into cur level.
    
    add curLevel to result.

"""
