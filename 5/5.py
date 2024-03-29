# Google FooBar Challenge 5
# Python 2.7.13
# Forbidden Imports: bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib

from fractions import Fraction, gcd

# Holy shit that was a tough one. 
# I failed test case 9 at first and its either because my LCM was wrong or because I didnt test for n == 1

# God, just let me use libs...
def inv(matrix):
    n = len(matrix)
    inverse = [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]
    for i in range(n):
        f = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= f
            inverse[i][j] /= f
        for k in range(n):
            if k != i:
                f = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= f * matrix[i][j]
                    inverse[k][j] -= f * inverse[i][j]
    return inverse

def mm(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def lcm(mat):
    curr = mat[0]
    for n in mat[1:]:
        curr = curr * n // gcd(curr, n)
    return curr

def solution(m):
    n = len(m)
    if n == 1:
        return [1, 1]
    states = [i for i, row in enumerate(m) if sum(row) == 0]
    Q, R = [], []
    for i in range(n):
        if i not in states:
            qr = []
            rr = []
            row_sum = sum(m[i])
            for j in range(n):
                if j not in states:
                    qr.append(Fraction(m[i][j], row_sum))
                else:
                    rr.append(Fraction(m[i][j], row_sum))
            Q.append(qr)
            R.append(rr)
    neq = [[Fraction(int(i==j), 1) - Q[i][j] for j in range(len(Q))] for i in range(len(Q))]
    N = inv(neq)
    B = mm(N, R)
    init = B[0]
    lcmden = lcm([frac.denominator for frac in init])
    r = [frac.numerator * (lcmden // frac.denominator) for frac in init]
    r.append(lcmden)
    return r

print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])) # [7, 6, 8, 21]
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])) # [0, 3, 2, 9, 14]
