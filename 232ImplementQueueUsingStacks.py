#leetcode 232. Implement Queue using Stacks
#https://leetcode.com/problems/implement-queue-using-stacks/
#스택을 이용해 push(x), pop(), peek(), empty() 연산을 지원하는 큐 구현

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []