# Google FooBar OPTIONAL Challenge 2
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def solution(l):
    l.sort()
    mod = sum(l) % 3
    if mod == 0:
        l.sort(reverse=True)
        return int(''.join(map(str, l))) if l else 0
    mod1 = [i for i, val in enumerate(l) if val % 3 == 1]
    mod2 = [i for i, val in enumerate(l) if val % 3 == 2]
    if mod == 1:
        if mod1:
            l.pop(mod1[0])
        else:
            l.pop(mod2[1])
            l.pop(mod2[0])
    elif mod == 2:
        if mod2:
            l.pop(mod2[0])
        else:
            l.pop(mod1[1])
            l.pop(mod1[0])
    l.sort(reverse=True)
    return int(''.join(map(str, l))) if l else 0

print(solution([3, 1, 4, 1])) # 4311
print(solution([3, 1, 4, 1, 5, 9])) # 94311
