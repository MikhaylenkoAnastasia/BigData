from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield str("fizzbuzz")
        elif i % 3 == 0:
            yield str("fizz")
        elif i % 5 == 0:
            yield str("buzz")
        else:
            yield str(i)