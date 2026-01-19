"""
*** Min Stack ***

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


from typing import Optional


class MinStack:
    def __init__(self) -> None:
        self._min_values_stack: list[int] = []
        self._stack: list[int] = []

    @property
    def _min_value(self) -> int:
        return self._min_values_stack[-1]

    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._min_values_stack or val <= self._min_value:
            self._min_values_stack.append(val)

    def pop(self) -> None:
        removed = self._stack.pop()
        if removed == self._min_value:
            self._min_values_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> Optional[int]:
        return self._min_value


def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    min_stack.getMin()  # return -3
    min_stack.pop()
    min_stack.top()  # return 0
    min_stack.getMin()  # return -2


if __name__ == "__main__":
    main()
