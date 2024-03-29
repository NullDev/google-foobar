# Google FooBar Challenge 3
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def base(num, b, length):
    n = ''
    while num > 0:
        num, rem = divmod(num, b)
        n = str(rem) + n
    return n.zfill(length)

def solution(n, b):
    k = len(n)
    seen = {}
    while n not in seen:
        seen[n] = len(seen)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z = int(x, b) - int(y, b)
        n = base(z, b, k)
    return len(seen) - seen[n]

print(solution('1211', 10)) # 1
print(solution('210022', 3)) # 3
