# Google FooBar OPTIONAL Challenge 6
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from fractions import Fraction

def solution(pegs):
    if len(pegs) < 2: return [-1, -1]
    for e in xrange(1, pegs[1] - pegs[0]):
        g, valid = [e], True
        for peg in xrange(1, len(pegs)):
            nxt = pegs[peg] - (pegs[peg - 1] + g[-1])
            if nxt <= 0:
                valid = False
                break
            g.append(nxt)
        if valid:
            l = Fraction(g[-1] * 2)
            if e == l:
                return [e, 1]
            if e + 1 == l:
                return [(e * 3) + 1, 3]
            if e + 2 == l:
                return [(e * 3) + 2, 3]
    return [-1, -1]

print(solution([4, 17, 50])) # -1,-1
print(solution([4, 30, 50])) # 12,1
