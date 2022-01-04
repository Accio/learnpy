"""
This is a module that I make for learning doctest

The module supplies one function, fib(). For example,

>>> fib(3)
2
"""


def fib(n: int):
    """Return the nth Fibonacci number, n is an integer >= 0

    >>> [fib(n) for n in range(6)]
    [0, 1, 1, 2, 3, 5]
    >>> fib(12)
    144
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if n + 1 == n:  # a very large number
        raise OverflowError("n is too large")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 1  # f(n-2)
    b = 1  # f(n-1)
    for i in range(2, n):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
