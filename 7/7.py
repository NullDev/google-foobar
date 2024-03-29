# Google FooBar Challenge 7
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from collections import deque

# Ew, graph math

def bfs(rG, s, t, p):
    seen = [False] * len(rG)
    q = deque([s])
    seen[s] = True
    while q:
        u = q.popleft()
        for ind, val in enumerate(rG[u]):
            if not seen[ind] and val > 0:
                if ind == t:
                    p[ind] = u
                    return True
                q.append(ind)
                seen[ind] = True
                p[ind] = u
    return False

def edmondskarp(g, source, sink):
    rG = [x[:] for x in g]
    p = [-1] * (len(g))
    mf = 0
    while bfs(rG, source, sink, p):
        pf = float('inf')
        s = sink
        while s != source:
            pf = min(pf, rG[p[s]][s])
            s = p[s]
        mf += pf
        v = sink
        while v != source:
            u = p[v]
            rG[u][v] -= pf
            rG[v][u] += pf
            v = p[v]
    return mf

def solution(entrances, exits, path):
    N = len(path)
    g = [[0] * (N + 2) for _ in range(N + 2)]
    src = N
    s = N + 1
    for i in range(N):
        for j in range(N):
            g[i][j] = path[i][j]
    for e in entrances:
        g[src][e] = float('inf')
    for e in exits:
        g[e][s] = float('inf')
    return edmondskarp(g, src, s)

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])) # 6
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])) # 16
