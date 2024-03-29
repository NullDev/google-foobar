# Google FooBar OPTIONAL Challenge 1
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from collections import defaultdict

def gen(c1, c2, len):
    a = c1 & ~(1 << len)
    b = c2 & ~(1 << len)
    c = c1 >> 1
    d = c2 >> 1
    return (a & ~b & ~c & ~d) | (~a & b & ~c & ~d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)

def mapper(n, a):
    m = defaultdict(set)
    a = set(a)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            g = gen(i, j, n)
            if g in a:
                m[(g, i)].add(j)
    return m

def solution(g):
    g = list(zip(*g))
    cols = len(g[0])
    a = [sum([1 << i if col else 0 for i, col in enumerate(row)]) for row in g]
    m = mapper(cols, a)
    r = { i: 1 for i in range(1 << (cols + 1))}
    for row in a:
        nxt = defaultdict(int)
        for c1 in r:
            for c2 in m[(row, c1)]:
                nxt[c2] += r[c1]
        r = nxt
    return sum(r.values())

print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])) # 11567
print(solution([[True, False, True], [False, True, False], [True, False, True]])) # 4
print(solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])) # 254
