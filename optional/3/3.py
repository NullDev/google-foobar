# Google FooBar OPTIONAL Challenge 3
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def top(query, node, level):
    if level == 1: return -1
    l = node - (2 ** (level - 1) - 1) - 1
    r = node - 1
    if query == l or query == r: return node
    if query < l: return top(query, l, level - 1)
    else: return top(query, r, level - 1)

def solution(h, q):
    return [top(x, 2 ** h - 1, h) for x in q]

print(solution(5, [19, 14, 28])) # 21,15,29
print(solution(3, [7, 3, 5, 1])) # -1,7,6,3
