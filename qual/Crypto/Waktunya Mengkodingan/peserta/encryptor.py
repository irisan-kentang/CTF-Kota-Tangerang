#!/usr/bin/python3

m = input("Masukkan teks: ")
k1 = int(input("Masukkan kunci angka 1: "))
k2 = int(input("Masukkan kunci angka 2: "))

m = [ord(i) for i in list(m)]
k1 = k1 % 255
k2 = k2 % 255

d = []
for i in m:
    d.append(chr(i ^ k1))
    k1 = (k1 + k2) % 255

d = ''.join(d)
print("Hasil enkripsi: ", d.encode('utf-8').hex())