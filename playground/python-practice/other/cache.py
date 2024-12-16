def factorial(n):
    if n <= 0:
        return n
    return n + factorial(n - 1)


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(factorial(5))
print(factorial(5))

fib_gen = fib_generator()
for _ in range(10):
    print(next(fib_gen))
