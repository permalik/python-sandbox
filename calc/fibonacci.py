def v1(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    return v1(n - 1) + v1(n - 2)
