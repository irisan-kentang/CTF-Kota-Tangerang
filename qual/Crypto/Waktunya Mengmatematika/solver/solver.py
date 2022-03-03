#!/usr/bin/python3

d = "c6bdcc86c6b1cbb4c6a1cb9dc691cb81c6a0cb99c781cc93c69ecb9bc6a8cba3c781cc8ec6a8cba3c785cc96c6a2cb99c681caa3c691cb81c689cab3c6b4cbb9c6a6cba3c682caa3c6b5cbbac6becc8ec6a9cba9c6b2cbbd"
d = bytes.fromhex(d).decode('utf-8')

# matrix [[a, b], [c, d]]
mat = [[3, 1], [5, 2]]

def inverse_matrix(m):
    a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]

imat = inverse_matrix(mat)

def multiply(m):
    a, b, c, d = imat[0][0], imat[0][1], imat[1][0], imat[1][1]
    e, g, f, h = m[0][0], m[0][1], m[1][0], m[1][1]
    return [[a*e + b*g, c*e + d*g], [a*f + b*h, c*f + d*h]]


d = [ord(i) for i in list(d)]
d = [d[i:i+2] for i in range(0, len(d), 2)]

m1 = []
for i in range(0, len(d), 2):
    m1 += (i for i in multiply(d[i:i+2]))

m2 = []
for i in m1:
    for j in i:
        m2 += [j]

m = ''.join(chr(int(i)) for i in m2)
print("FLAG: ", m)