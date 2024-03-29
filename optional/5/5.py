# Google FooBar OPTIONAL Challenge 5
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    pos = [x for x in xs if x > 0]
    negs = [x for x in xs if x < 0]

    if not pos and len(negs) < 2:
        return "0"

    if len(negs) % 2 != 0:
        negs.remove(max(negs))

    result = 1
    for n in pos + negs:
        result *= n

    return str(result)

print(solution([2, 0, 2, 2, 0])) # 8
print(solution([-2, -3, 4, -5])) # 60
