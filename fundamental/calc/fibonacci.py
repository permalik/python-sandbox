def fibonacci_v1(args):
    def execute(n):
        if n == 0:
            return n
        if n == 1:
            return n
        return execute(n - 1) + execute(n - 2)

    for i in range(args.iterations):
        print(execute(i), end=" ")
    print("")
