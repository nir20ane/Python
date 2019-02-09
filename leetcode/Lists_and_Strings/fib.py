def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print fib(5)
print map(fib, range(0, 10))

