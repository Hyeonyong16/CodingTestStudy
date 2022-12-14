#leetcode 225. Implement Stack using Queues
#https://leetcode.com/problems/implement-stack-using-queues/
#큐를 이용해 push(x), pop(), top(), empty() 연산을 지원하는 스택 구현

import collections

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0