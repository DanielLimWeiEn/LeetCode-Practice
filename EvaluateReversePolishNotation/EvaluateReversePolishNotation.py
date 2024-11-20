class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        deltas = {
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : x - y,
            "*" : lambda x, y : x * y,
            "/" : lambda x, y : x // y if x >= 0 and y >= 0 else (abs(x) // abs(y) if x < 0 and y < 0 else -1 * (abs(x) // abs(y)))
        }

        for token in tokens:
            if token not in deltas:
                stack.append(int(token))
            if token in deltas:
                second = stack.pop()
                first = stack.pop()
                result = deltas[token](first, second)
                stack.append(int(result))
        return stack.pop()

"""

Ok, reverse polish notation. I feel like I can use a stack for this.

use a stack.

1. iterate over every element in the tokens list.

if a number -> push onto stack.

if operand -> pop 2 off the stack, operate, push onto the stack.

finally, return the value at the top of the stack.

"""
