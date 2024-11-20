# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        inOrderRes = []

        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.left)
                inOrderRes.append(root.val)
                inOrderTraversal(root.right)
        
        inOrderTraversal(root)

        for i in range(1, len(inOrderRes)):
            if inOrderRes[i] <= inOrderRes[i - 1]:
                return False
        print(inOrderRes)
        
        return True

"""

Ok. so validate a binary search tree.

Key ideas,

at each node, node.left < node < node.right

if node: return True
if None: return True


"""
