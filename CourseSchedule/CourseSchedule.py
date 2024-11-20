class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set() # maintain a set of visited elements.

        # convert the prerequisites representation into an adjacency list representation that
        # is easier to work with.
        adjacencyList = { i : [] for i in range(0, numCourses) }
        for course, prerequisite in prerequisites:
            adjacencyList[course].append(prerequisite)
        
        def dfs(course) -> bool:
            if course in visited: # if we have visited this element before in the current iteration, i.e. cycle.
                return False
            if not adjacencyList[course]: # if the course has no prerequisites, then it can be completed.
                return True
            
            visited.add(course)
            
            for neighbor in adjacencyList[course]: # go over the prerequisites and check if they are completable.
                if not dfs(neighbor):
                    return False
            
            visited.remove(course)
            adjacencyList[course] = [] # if we make it here, then all the prerequisites are completable.
            return True
        
        res = True
        for course in adjacencyList:
            res = res and dfs(course)
        
        return res



"""

Ok, course scheduling.

Idea: A directed graph G contains a cycle if and only if there is a back edge. We are making use of this lemma for this algorithm.

So idea, dfs, and maintain the visited stack, to keep track of all the nodes that have been visited. If at any point, we find that there is an edge from the current to a node in the visited array, then we return false that it is impossible to finish all courses. Otherwise, we return true.

So the representation.

def dfs(curNode):
    visited.add(curNode)

    find Neighbors -> iterate over prerequisites and find edges out of this curNode and call dfs on them. before that, if the edge is going into a visited node, then we return false.

    return true otherwise.

findNeighbors -> we have the adjacency list so we go over the neighbors directly.

Now, for a particular node, we want to mark whether the course can be completed.
The way that we will do this is we will check whether the course has no prerequisites.
So dfs returns true if can be compeleted else returns false.

ok, so we are going to be using an adjacency list.

What is it exactly that we want to do?

We want to find out whether each course is completable of the n courses. OK. For each of those courses.

dfs(course) -> boolean: # answers the question, can this course be completed?
    if course neighbors == []:
        return True
    
    for neighbor in neighbors:
        if dfs(neighbor):
            course.neighbors.remove(neighbor)

there is one more thing that we have to keep track of. that is the set of visited elements.

"""
