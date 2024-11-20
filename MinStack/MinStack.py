class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        """
        1. Push onto the stack as regular.
        2. Maintain the min element of the stack.
        """
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        """
        1. Pop off from the stack as regular.
        2. Maintain the min element of the stack.
        """
        topVal = self.stack.pop()
        self.minStack.pop()
        return topVal

    def top(self) -> int:
        """
        1. Get the top element of the stack.
        """
        return self.stack[-1]
        

    def getMin(self) -> int:
        """
        1. Get the min element of the stack.
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()