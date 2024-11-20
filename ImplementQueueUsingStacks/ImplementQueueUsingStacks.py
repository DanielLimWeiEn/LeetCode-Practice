# What are the functionalities of a Queue
# push: push onto the end of a queue
# pop: pop a value from the front of the queue
# peek: peek the value from the top of the queue
# empty: checks if the queue is empty

# What are the functionalities of a Stack
# push: push onto the end of a stack
# pop: pop a value from the end of the stack
# peek: peek the value from the end of the stack
# empty: checks if the queue is empty

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        else:
            return self.stack2[-1]
        
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()