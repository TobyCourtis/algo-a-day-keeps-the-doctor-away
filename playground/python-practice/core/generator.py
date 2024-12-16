def simple_range(limit):
    for i in range(limit):
        yield i


for num in simple_range(5):
    print(num)  # Output: 0 1 2 3 4

print("-----")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()
for _ in range(7):
    print(next(fib_gen))  # Output: 0 1 1 2 3 5 8
