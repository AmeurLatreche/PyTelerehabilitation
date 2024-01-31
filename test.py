import time


def fib(cnt):
    n, a, b = 0, 0, 1
    while n < cnt:
        yield a
        a, b = b, a + b
        n = n + 1

g = fib(10)
for i in range(10):
    # time.sleep()
    print(g.__next__())