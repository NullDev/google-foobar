# Google FooBar Challenge 2
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def solution(s):
    r = 0
    for i in range(len(s)):
        if s[i] == '>':
            for j in range(i + 1, len(s)):
                if s[j] == '<':
                    r += 2
    return r

print(solution('>----<')) # 2
print(solution('<<>><')) # 4
print(solution('--->-><-><-->-')) # 10
