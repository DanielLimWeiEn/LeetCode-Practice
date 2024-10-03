# LeetCode Grinding Notes

## 15 Common LeetCode Patterns To Learn

Take reference from the video at [LeetCode was HARD until I Learned these 15 patterns](https://www.youtube.com/watch?v=DjYZk8nrXVY)

### 1. Prefix Sum

Used to query sum of elements in a subarray.

```javascript
Array = [1, 2, 3, 4, 5, 6, 7]
         ^        ^
         i        j

An array of n elements is given like so, and you want to query sum of elements between indices i and j.

With a single search query, this is easy and can be done in O(n) time.

With multiple search queries, imagine i and j constantly change, this is difficult and can take O(n * m) time where m is number of queries.

SOLUTION: use a prefix sum array to make this faster

PREFIX = [1, 3, 6, 10, 15, 21, 28]

PREFIX[i] = Array[0] + Array[1] + ... + Array[i] -> Each ith element is the sum of elements from index 0 to i in the original array.

Sum[i, j] = PREFIX[j] - PREFIX[i - 1] -> General formula for the sum from ith to jth element in Array.

```

Tip: You can use an input array to avoid using any additional space.

### 2. Two Pointers

Initialize two pointers and move them along an iterable object. Either move them towards each other or move them away from each other.

```javascript
Array = [1, 2, 3, 4, 5, 6, 7]
         ^                 ^
         i->             <-j

Used for reducing the time complexity of problems from O(n^2) to O(n).


String = "abcdcba"

Suppose that you want to check whether a string is a palindrome as above.

i points to index 0. j points to index String.length() - 1.

At each step, you check whether String[i] is equal to String[j]. If they are, then move i inward (i++) and move j inward (j--).

If ever, the characters do not match, then the string is not a palindrome.

If the two pointers cross, then the string is a palindrome.
```

### 3. Sliding Window

Used to find subarrays of substrings that meet a specific criteria.

```javascript
Array = [3, 2, 7, 5, 9, 6, 2] with K = 3
         ^->   ^->

Find a subarray of size K of maximum sum from the array of size n.

The brute force solution involves using nested for loops to find every subarray of size K. O(n * K) which is inefficient.

Notice that for each subarray of size K, there is a lot of repeated characters.

Only 1 character is changed each time.

The idea is to maintain the sum of the elements in the current window.

And maintain the max sum subarray.

As the window progresses, you deduct the value that was just taken out and you add the value that was just added to the sliding window.

Then do a comparison and check whether the new sliding window value exceeds the max value previously found.

This reduces the time complexity from O(n * K) to O(n), since we are only doing a single iteration through the array.
```

### 4. Fast and Slow Pointer

Variant of the two pointers approach. Used to solve problems related to linked lists and arrays which involve finding cycles. Works by moving two pointers at different speeds.

```javascript
LinkedList = [1] -> [3] -> [5] -> [7] -> [9]
                                   ^      |
                                   |  <-  v

Initialize fast and slow to point to the start.

Iterate, and move the slow pointer 1 element at a time, and the fast pointer 2 elements at a time.

If there is a cycle, the two pointers eventually meet. Otherwise, the slow element will each the end.

This can also be used to find the middle element of a linked list in a single pass, when the fast pointer reaches the end, the slow pointer is at the middle of the linked list.
```

### 5. Linked List In-Place Reversal

Many linked list questions require you to manipulate the nodes and pointers of the linked list in some way. The tricky part is doing it in-place without using any extra space.

```javascript
LinkedList = [1] -> [3] -> [5] -> [7] -> [9]

Prev = null
Current = LinkedList.head

While current is not Null:
    next = current.next
    current.next = prev
    prev = current
    current = next

return prev

Use the 3 variables above. The basic idea follows.

Loop:
    Set next to the next node of current node in the original linked list.
    Set the current node to have its next node point to the previous node in new order.
    Progress previous to the current node in question in new order.
    Set current node to be the stored next node in original linked list order.

At the end, the previous node points to the head of the new linked list and we are done.
```

### 6. Monotonic Stack

Uses a stack to find the next greater or next smaller element in the array.

```javascript
Given the array, find the next greater element for each item and output an array. If there isn't one, output -1.

Array = [1, 4, 6, 3, 2, 7]

The brute force way to do this is using a nested for loop. For each element, we scan through all the remaining elements, and find the next greater element.

This is O(n^2)

This can be solved using a stack.

Stack tracks the indices of elements in the array for which we haven't found the next greater element yet.

Iterate through the elements in the array. For each element, check if the value is greater than that at the top of the stack. If it is, continuously pop from the stack and set the result from that index to that current element in the array. Then push the current element index onto the stack. During the entire process, we keep the stack elements in only decreasing order in this case as we are finding the next greater element. If we are finding the next smaller element, keep the stack elements in increasing order.
```

### 7. Top 'K' Elements

Used for finding the 'K' Largest, Smallest or Most Frequent Elements in a dataset.

```javascript
Array = [1, 5, 11, 9, 7, 2]

Suppose that you want to find the K largest elements in the array.

The easiest way to solve this is to sort the array, and then return the first K elements. This is O(n log n) runtime.

To avoid sorting, we can use a min-heap with K elements.

With a min-heap, insertion and addition takes O(log K) time, where K is the number of nodes in the min-heap.

We iterate over every element in the array, and then with each element we compare the value with the min value in the heap which is O(1). If the value is greater, then we remove the min element from the min-heap O(log K) and then insert the new element into the min-heap O(log K). Using this, we can maintain at all times the K largest elements in the dataset.

With this, we reduce the runtime from O(n log n) to O(n log K).
```

If the problem asks for the K largest elements, use a min-heap. If the problem asks for the K smallest elements, use a max-heap.

### 8. Overlapping Intervals

Used for problems involving ranges or intervals that may overlap.

Here are a few problem types in which you can apply this pattern:
* merging intervals - merge all the overlapping intervals into one
* interval intersection - find the intersection between two sets of intervals
* insert interval - add a new interval into a list of non-overlapping intervals
* find the mimimum number of meeting rooms for overlapping meeting times

```javascript
Merge all the overlapping intervals in the list of intervals given below.

ListOfIntervals = [ [2, 6], [1, 3], [8, 10], [15, 18] ]

First, sort the intervals by start time. O(n log n) time.

Second, create an empty array to store the merged intervals. O(n) space.

Third, iterate over the sorted list of intervals. For each interval do the following.
    if first element -> store the interval in the mergedIntervals array.
    if SortedListOfIntervals[current].first <= MergedListOfIntervals[last].second -> update MergedListOfIntervals[last].second to be SortedListOfIntervals[current].second. (this means that there is overlap)
    else if there is no overlap -> add the SortedListOfIntervals[current] to the MergedListOfIntervals
```

Tips: Standard format -> Sort, Merge, Return

### 9. Modified Binary Search

Is a variant of the regular binary search pattern, and this is used to solve problems in which a given array is not perfectly sorted.

Here are some problems in which you can use this pattern:
* Saerching in a nearly sorted array
* Searching in a rotated sorted array
* Searching in a list with unknown length
* Searching in an array with duplicates
* Finding the first or last occurence of an element
* Finding the square root of a number
* Finding a peak element

```javascript
const RotatedSortedArray = [4, 5, 6, 7, 0, 1, 2]

function searchRotatedArray(nums, target) {
    let left, right = 0, len(nums - 1)

    while (left <= right) {
        mid = (left + right) / 2 // floor division

        if (nums[mid] === target) {
            return mid
        }

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
    }

    return -1
}

Suppose we are given a rotated sorted array and we need to search for an element. We can perform binary search with a few additional checks to determine which half of the array is sorted. Within that check, we check if the target is within the range of the sorted half. If it is, we search that half, otherwise, we search the other half.
```

### 10. Binary Tree Traversal

Binary Trees are all about traversing them in a specific order.

Here are the 4 most popular orders of traversing a binary tree:
* Preorder - root first, search left, search right
* Inorder - search left, root next, search right
* Postorder - search left, search right, root last
* Level Order - level by level

```javascript
function preorderTraversal(node) {
    if node:
        print(node.value)
        preorderTraversal(node.left)
        preorderTraversal(node.right)
}

function inorderTraversal(node) {
    if node:
        inorderTraversal(node.left)
        print(node.value)
        inorderTraversal(node.right)
}

function postorderTraversal(node) {
    if node:
        postorderTraversal(node.left)
        postorderTraversal(node.right)
        print(node.value)
}

function levelorderTraversal(node) {
    if not node:
        return []
    
    const result = []
    const queue = new Queue()

    while queue:
        const sizeOfLevel = queue.length()
        const currentLevel = []

        for (let i = 0; i < sizeOfLevel; i++) {
            node = queue.removeFromHead()
            currentLevel.add(node.val)

            if node.left:
                queue.addToQueueFromBack(node.left)
            if node.right:
                queue.addToQueueFromBack(node.right)
        }

        result.append(currentLevel)
    
    return result
}
```

Tips: When you are given a tree problem, think about which traversal order fits the best.

For example:
* To retrieve the values of a binary search tree in sorted order, use inorder traversal.
* To create a copy of the tree (serialization) use preorder traversal.
* When you want to process child nodes before the parent nodes, such as when deleting a tree, use postorder traversal.
* When you need to explore all nodes at a current level before moving on to the next, use level order traversal.

### 11. Depth First Search (DFS)

It is used to explore all paths or branches in graphs or trees.

Here are some examples of problems that DFS can be used to solve:
* Finding a path between 2 nodes.
* Checking if a graph contains a cycle.
* Finding a topological order in a Directed Acyclic Graph (DAG).
* Counting the number of connected components in a graph.

```javascript
function dfsRecursive(node, visited) {
    visited.add(node)
    print(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfsRecursive(neighbor, visited)
}

function dfsIterative(node) {
    visited = set()
    stack = [node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            print(current)

            for neighbor in reversed(current.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
}

The generic approach to solving DFS related problems is like so:

First, choose a starting point.

Second, keep track of the visited nodes to avoid cycles.

Third, perform the required operation on the currently visiting node.

Fourth, explore unvisited neighbors.

Repeat until all the nodes have been explored.
```

### 12. Breadth First Search (BFS)

BFS is a traversal technique that is used to explore the nodes in a graph or tree level by level.

Here are some examples of problems that BFS can be used to solve:
* Finding the shortest path between two nodes in an unweighted graph.
* Printing all the nodes of a tree level by level.
* Finding all connected components in a graph.
* Finding the shortest transformation sequence from one word to another.

```javascript
function BFS(startNode) {
    visited = set()
    queue = []

    visited.add(startNode)

    while queue:
        frontOfQueue = queue.popLeft()
        print(frontOfQueue)

        for (neighbor in frontOfQueue.neighbors) {
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        }
}

The generic approach to solving BFS is as such:

First, add the starting node to the queue.

Second, set up the visited set.

Third, continue while the queue is not empty,

Fourth, dequeue a node from the front of the queue and process is.

Fifth, enqueue the unvisited neighbors of said node.

Repeat until the queue is empty, signifying all the nodes in the graph have been explored.
```

### 13. Matrix Traversal

Most matrix traversal problems can be seen as graph problems.

In a graph, you have nodes and edges. In a matrix, we usually have a 2D array where the nodes are the cells from where you can reach to adjacent cells horizontally, vertically or diagonally depending on the problem. The best part is that you can use most of the graph traversal algorithms such as DFS and BFS to solve the matrix related problems.

Here are some matrix traversal problems that can be solved using graph traversal algorithms:
* Finding the shortest path in a grid (Djikstra's Shortest Path Algorithm)
* Counting the number of islands (Counting connected components)

```javascript
const grid = [
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
]

1 represents land. 0 represents water.

You need to find the number of islands. An island is formed by connecting adjacent lands either vertically or horizontally.

We can use either DFS or BFS to solve this problem.

function countIslands(grid) {
    if not grid or not grid[0]:
        return 0
    
    const rows, cols = len(grid), len(grid[0])
    let islands = 0

    function dfs(i, j) {
        if (i < 0 || i >= rows || j < 0 || j >= cols or grid[i][j] != '1') {
            return
        }

        grid[i][j] = '0' // mark as visited, although other ways are possible that use more space.

        dfs(i + 1, j) // down
        dfs(i - 1, j) // up
        dfs(i, j + 1) // right
        dfs(i, j - 1) // left
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] == '1') {
                dfs(i, j)
                islands += 1
            }
        }
    }

    return islands
}
```

Tips: Model the matrix as a graph. The cells are nodes. Then there are surrounding cells, those are reachable from the node in question via edges. Once you have this model, you can use a graph traversal algorithm to solve this.

### 14. Backtracking

Backtracking is a powerful technique used to solve problems that involve exploring all potential solution paths and backtracking the paths that do not lead to a valid solution.

Here are some problems that can be solved using the backtracking algorithms:
* Generate all possible permutations/combinations of a given set of elements.
* Solve puzzles likes Sudoku or the N-Queens Problem.
* Find all possible paths from start to end in a graph or a maze.
* Generate all valid parentheses of a given length.

```javascript
Suppose we are given the following and the task is to generate all the possible subsets. We can use backtracking to solve this problem.

const set = [1, 2, 3]

Start with an empty subset. Then we iterate over each element in the array. For each element, we have 2 choices, either we include the element in the subset or we do not. After making a choice, we recurse to the next element. Once we have considered all elements, we backtrack to explore other possibilities.
```

### 15. Dynamic Programming (DP)

Dynamic Programming (DP) is a technique used for solving optimization problems by breaking the problem down into smaller sub problems, solving those sub problems optimally, and then storing the solutions to avoid repetitive work. It is based on the idea that the solution to the big problem is the sum of the optimal solutions to the sub problems.

It is particularly useful for problems which have the following properties:
* Overlapping Subproblems.
* Optimal Substructure.

Here are some examples of problems which have said properties and that can be solved using dynamic programming:
* Maximize or Minimize a Certain Value
* Counting Problems where we have to Count the Number of Ways to Achieve a Certain Goal

DP is a big and challenging topic for coding interviews. Learning it can be made easier if we learn some common patterns:
* Fibonacci Numbers
* 0/1 Knapsack
* Longest Common Subsequence (LCS)
* Longest Increasing Subseqquence (LIS)
* Subset Sum
* Matrix Chain Multiplicatio

