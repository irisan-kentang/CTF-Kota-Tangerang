#!/usr/bin/python3

d = "c6bdcc86c6b1cbb4c69acb8dc6b7cbbcc6b1cbb4c6b0cbb5c6bdcc86c79ecd81c697cb8dc69ccb93c697cb8dc6a6cba3c682caa3c68dcab6c6a9cba4c6b3cbbac69ecb95c6a2cb99c68dcabbc69dcb95c785cc96c6b1cbb4c697cab1c280c3a0"
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