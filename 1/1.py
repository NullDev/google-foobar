# Google FooBar Challenge 1
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def solution(x, y):
    return list(set(x).symmetric_difference(set(y)))[0]

print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])) # -4
print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13])) # 6
