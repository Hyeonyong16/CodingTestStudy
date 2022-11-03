#leetcode 622. Design Circular Queue
#https://leetcode.com/problems/design-circular-queue/
#원형큐 구현

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.frontP = 0
        self.rearP = 0

    #값을 큐에 넣을 수 있으면 넣고 true 반환
    def enQueue(self, value: int) -> bool:
        if self.q[self.rearP] is None:
            self.q[self.rearP]  = value
            self.rearP = (self.rearP + 1) % self.maxlen
            return True
        else:
            return False       

    #큐에서 값을 뺄 수 있으면 빼고 true 반환
    def deQueue(self) -> bool:
        if self.q[self.frontP] is None:
            return False
        else:
            self.q[self.frontP] = None
            self.frontP = (self.frontP + 1) % self.maxlen
            return True

    #front는 맨앞의 값이니까 frontP에 있는 값 반환하면 됨
    def Front(self) -> int:
        if self.q[self.frontP] is None:
            return -1
        else:
            return self.q[self.frontP]

    #rear는 맨뒤의 값인데 rearP는 값보다 하나 뒤를 가르키므로 -1 해주어야 함
    def Rear(self) -> int:
        if self.q[self.rearP - 1] is None:
            return -1
        else:
            return self.q[self.rearP - 1]

    def isEmpty(self) -> bool:
        if self.frontP == self.rearP and self.q[self.frontP] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.frontP == self.rearP and self.q[self.frontP] is not None:
            return True
        else:
            return False