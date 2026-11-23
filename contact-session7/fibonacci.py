def fibonacci(n):
    """Return the first n numbers of the Fibonacci series."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


n = int(input("How many Fibonacci numbers? "))
print(fibonacci(n))
