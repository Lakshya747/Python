from __future__ import annotations

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    d, x, y = extended_gcd(b, a % b)
    return d, y, x - (a // b) * y

def diophantine(a: int, b: int, c: int) -> tuple[float, float]:
    d = gcd(a, b)
    assert c % d == 0
    x, y = extended_gcd(a, b)[1:]
    r = c / d
    return r * x, r * y

def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> None:
    x0, y0 = diophantine(a, b, c)
    p, q = a // gcd(a, b), b // gcd(a, b)
    for i in range(n):
        print(x0 + i * q, y0 - i * p)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
