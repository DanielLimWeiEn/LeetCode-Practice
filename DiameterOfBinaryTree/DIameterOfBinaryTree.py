# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = [0]

        def findHeightOfBinaryTree(root, max_diameter):
            if root is None:
                return 0
            
            left_height = findHeightOfBinaryTree(root.left, max_diameter)
            right_height = findHeightOfBinaryTree(root.right, max_diameter)
            height = max(left_height, right_height) + 1
            
            max_diameter[0] = max(left_height + right_height, max_diameter[0])

            return height
        
        findHeightOfBinaryTree(root, max_diameter)
        return max_diameter[0]

"""
Diameter is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

So we know about height of a binary tree.

h_null = 0
h_leaf = 0
height = max(height_of_left, height_of_right) + 1
"""
