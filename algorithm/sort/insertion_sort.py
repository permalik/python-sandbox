import random


def insertion_sort_v1(args):
    list = [random.randint(1, 100) for _ in range(args.length)]
    target = random.randint(1, 100)

    def execute(l):
        low = 0
        high = len(l)
        while low <= high:
            mid = (high + 1) // 2
            if l[mid] == target:
                return mid
            if l[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    result = execute(list)

    for i in list:
        print(i, end=" ")

    print(result)
