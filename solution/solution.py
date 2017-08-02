def solved_fib(n):
    if n < 2:
        return 1
    else:
        return solved_fib(n - 1) + solved_fib(n - 2)