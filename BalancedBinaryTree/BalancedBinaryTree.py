# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recurse(root):
            if not root: # null
                return 0, True
            
            heightLeftSubtree, isLeftSubtreeHeightBalanced = recurse(root.left)
            heightRightSubtree, isRightSubtreeHeightBalanced = recurse(root.right)
            isCurrentNodeBalanced = abs(heightLeftSubtree - heightRightSubtree) <= 1 and isLeftSubtreeHeightBalanced and isRightSubtreeHeightBalanced

            return 1 + max(heightLeftSubtree, heightRightSubtree), isCurrentNodeBalanced
        
        height, isTreeBalanced = recurse(root)

        return isTreeBalanced

# Think in terms of base cases,
# null is height-balanced.
# a single node is height-balanced.
# a single node with one node on either side is height-balanced.
# a single node with two nodes is height-balanced.

# What is the recursive case?
# a node is height balanced if both of it's subtrees are height-balanced and their heights don't differ
# by more than 1.
# it's possible to create 
        