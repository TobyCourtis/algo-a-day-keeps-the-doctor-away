class QueueFromStack:
    stackOne = []
    stackTwo = []

    # add item to queue
    def enqueue(self, item: int):
        while len(self.stackTwo) > 0:
            self.stackOne.append(self.stackTwo.pop())
        self.stackTwo.append(item)
        while len(self.stackOne) > 0:
            self.stackTwo.append(self.stackOne.pop())

    # remove first item from queue
    def dequeue(self) -> int:
        return self.stackTwo.pop() if len(self.stackTwo) > 0 else None


q = QueueFromStack()

q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
