class MyCircularQueue:

    def __init__(self, k: int):
        # Invariants:
        # r is at the enqueue position 
        # l points to the front of the queue

        self.l = 0
        self.r = 0
        self.q = [0] * k
        self.elements = 0
        self.capacity = k
        # enqueue from r
        # dequeue from l

    # [1, 0, 0]
    #  l  r
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.r] = value
        self.r = (self.r + 1) % self.capacity
        self.elements += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.l = (self.l + 1) % self.capacity
        self.elements -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.l]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.r - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.elements == 0

    def isFull(self) -> bool:
        return self.elements == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()