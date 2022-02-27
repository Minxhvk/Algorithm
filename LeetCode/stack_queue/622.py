class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.array = [None] * k
        self.front_idx = 0
        self.rear_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.array[self.rear_idx] is None:
            self.array[self.rear_idx] = value
            self.rear_idx = (self.rear_idx + 1) % self.max_size
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.array[self.front_idx] is None:
            return False
        else:
            self.array[self.front_idx] = None
            self.front_idx = (self.front_idx + 1) % self.max_size
            return True

    def Front(self) -> int:
        if self.array[self.front_idx] is None:
            return -1
        else:
            return self.array[self.front_idx]

    def Rear(self) -> int:
        if self.array[self.rear_idx - 1] is None:
            return -1
        else:
            return self.array[self.rear_idx - 1]

    def isEmpty(self) -> bool:
        if ((self.front_idx == self.rear_idx) and (self.array[self.front_idx] is None)):
            return True
        return False

    def isFull(self) -> bool:
        if ((self.front_idx == self.rear_idx) and (self.array[self.front_idx] is not None)):
            return True
        return False

        # Your MyCircularQueue object will be instantiated and called as such:
        # obj = MyCircularQueue(k)
        # param_1 = obj.enQueue(value)
        # param_2 = obj.deQueue()
        # param_3 = obj.Front()
        # param_4 = obj.Rear()
        # param_5 = obj.isEmpty()
        # param_6 = obj.isFull()
