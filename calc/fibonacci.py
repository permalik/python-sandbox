def v1_fibonacci(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    return v1_fibonacci(n - 1) + v1_fibonacci(n - 2)
