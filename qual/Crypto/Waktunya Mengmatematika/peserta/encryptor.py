#!/usr/bin/python3

m = input("Masukkan teks: ")

# padding
if len(m) % 4 != 0:
    m += " " * (4 - len(m) % 4)

# matrix [[a, b], [c, d]]
mat = [[3, 1], [5, 2]]

m = [ord(i) for i in list(m)]
m = [m[i:i+2] for i in range(0, len(m), 2)]

def multiply(m):
    a, b, c, d = mat[0][0], mat[0][1], mat[1][0], mat[1][1]
    e, g, f, h = m[0][0], m[0][1], m[1][0], m[1][1]
    return [[a*e + b*g, c*e + d*g], [a*f + b*h, c*f + d*h]]

d1 = []
for i in range(0, len(m), 2):
    d1 += (i for i in multiply(m[i:i+2]))

d2 = []
for i in d1:
    for j in i:
        d2 += [j]

d = ''.join(chr(i).encode('utf-8').hex() for i in d2)
print("Hasil enkripsi: ", d)