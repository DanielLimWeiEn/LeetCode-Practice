"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        def dfs(root):
            # clone the root
            clonedRoot = Node(root.val)

            # cache the root, we exploit the fact that each val is unique
            visited[root.val] = clonedRoot

            # iterate over the neighbors
            for neighbor in root.neighbors:
                if neighbor.val in visited:
                    clonedRoot.neighbors.append(visited[neighbor.val])
                else:
                    clonedRoot.neighbors.append(dfs(neighbor))
            
            # return the clonedRoot
            return clonedRoot
        
        clonedRoot = dfs(node)
        return clonedRoot

"""

Ok, so how do I approach this question?

I want to clone a graph. The way to do it is maintain a set of cloned elements.

The stored everything that has been visited in there. Start at the root, clone, visited, go over it's neighbours and recurse. for the neighbors, add the neighbor if the value is in the set. Or, I can use a map storing the val -> new Node.

"""
