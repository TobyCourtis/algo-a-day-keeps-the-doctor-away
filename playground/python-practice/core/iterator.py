class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):  # must implement in iterator
        return self

    def __next__(self):  # must implement in iterator
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1


for num in Countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1
