# Google FooBar Challenge 4
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

# I messed up the XOR at first and failed 3 test cases.

def xor(n):
    return [n, 1, n + 1, 0][n % 4]

def solution(start, length):
    r = 0
    for i in range(length):
        s = start + i * length
        e = s + (length - i) - 1
        r ^= xor(e) ^ xor(s - 1)
    return r

print(solution(0, 3)) # 2 
print(solution(17, 4)) # 14
