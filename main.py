# main.py
"""
python_curricula
"""

import argparse

from fundamental.calc.fibonacci import v1_fibonacci


def main():
    parser = argparse.ArgumentParser(description="python_curricula CLI")
    subparsers = parser.add_subparsers(
        dest="category", required=True, help="Select a Category"
    )

    """
    Fundamental Category
    """
    fun_parser = subparsers.add_parser("fun", help="Fundamental Programs")
    fun_subparsers = fun_parser.add_subparsers(dest="program", required=True)

    """
    Fundamental Category
    """
    fib_v1_parser = fun_subparsers.add_parser(
        "fibonacci_v1", help="Computer Fibonacci Sequence"
    )
    fib_v1_parser.add_argument(
        "-n", "--iterations", type=int, default=10, help="Number of iterations"
    )
    fib_v1_parser.set_defaults(func=v1_fibonacci)

    # parser.add_argument("con", help="Category: construct")
    # parser.add_argument("ds", help="Category: datastructure")
    # parser.add_argument("alg", help="Category: algorithm")
    #
    # """
    # Program Selection
    # """
    # parser.add_argument("program", help="Program to run")

    args = parser.parse_args()
    args.func(args)

    if args.program == "v1_fibonacci":
        for i in range(10):
            print(v1_fibonacci(i), " ", end="")


if __name__ == "__main__":
    main()
