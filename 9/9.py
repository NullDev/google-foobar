# Google FooBar Challenge 9
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from fractions import gcd
from math import factorial

def gp(n):
    r = set()
    r.add((n,))
    for x in range(1, n):
        for y in gp(n - x):
            r.add(tuple(sorted((x,) + y)))
    return r

def perm(c, n):
    p = factorial(n)
    for i in set(c):
        p /= (i**c.count(i)) * factorial(c.count(i))
    return p

def powmod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

mem = {}
def part(n, m):
    if (n, m) in mem:
        return mem[(n, m)]
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    mem[(n, m)] = part(n, m - 1) + part(n - m, m)
    return mem[(n, m)]

def solution(w, h, s):
    r = 0
    for wp in gp(w):
        for hp in gp(h):
            m = 1
            for i in wp:
                for j in hp:
                    m *= powmod(s, gcd(i, j), 10**20)
            r += perm(wp, w) * perm(hp, h) * m
    return str(r / (factorial(w) * factorial(h)))

print(solution(2, 3, 4)) # 430
print(solution(2, 2, 2)) # 7
