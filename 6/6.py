# Google FooBar Challenge 6
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

# WHY WAS THAT ONE SO EASY COMPARED TO THE PREVIOUS ONE?!

def solution(n):
    n = int(n)
    r = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        r += 1
    return r

print(solution('4')) # 2
print(solution('15')) # 5
