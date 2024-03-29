# Google FooBar Challenge 8
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from itertools import combinations

def solution(num_buns, num_required):
    r = [[] for _ in range(num_buns)]
    for i, c in enumerate(combinations(range(num_buns), num_buns - num_required + 1)):
        for j in c:
            r[j].append(i)
    return r

print(solution(4, 4)) # [[0], [1], [2], [3]]
print(solution(5, 3)) # [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
print(solution(2, 1)) # [[0], [0]]
