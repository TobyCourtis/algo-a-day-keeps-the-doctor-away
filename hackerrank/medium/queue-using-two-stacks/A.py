ENQUEUE_INDEX = 1
DEQUEUE_INDEX = 2
PRINT_FRONT_INDEX = 3


class QueueFromStacks:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    # add item to queue
    def enqueue(self, item: int):
        self.stackOne.append(item)

    # remove first item from queue
    def dequeue(self) -> int:
        if len(self.stackTwo) == 0:
            while len(self.stackOne) > 0:
                self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo.pop()

    def top(self):
        return self.stackTwo[-1] if len(self.stackTwo) > 0 else self.stackOne[0]


def main():
    queue = QueueFromStacks()

    n_commands = int(input().strip())
    for _ in range(n_commands):
        command_and_input = input().strip().split()
        command = int(command_and_input[0])
        if command == ENQUEUE_INDEX:
            value_to_queue = int(command_and_input[1])
            queue.enqueue(value_to_queue)
        elif command == DEQUEUE_INDEX:
            queue.dequeue()
        elif command == PRINT_FRONT_INDEX:
            print(queue.top())


if __name__ == '__main__':
    main()
