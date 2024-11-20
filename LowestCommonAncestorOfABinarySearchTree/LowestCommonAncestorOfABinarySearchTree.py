# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rootToP = []
        rootToQ = []
        
        def findPathFromRootTo(target, cur, arr):
            # Base Case
            if target.val == cur.val:
                arr.append(target)
                return

            # Recursive Case
            arr.append(cur)
            if target.val < cur.val:
                findPathFromRootTo(target, cur.left, arr)
            else:
                findPathFromRootTo(target, cur.right, arr)
        
        findPathFromRootTo(p, root, rootToP)
        findPathFromRootTo(q, root, rootToQ)

        print(rootToP)
        print(rootToQ)
        i = 0
        while i < min(len(rootToP), len(rootToQ)) and rootToP[i] == rootToQ[i]:
            i += 1
        
        return rootToP[i - 1]
