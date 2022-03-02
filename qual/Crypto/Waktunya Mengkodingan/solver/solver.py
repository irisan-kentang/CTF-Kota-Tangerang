#!/usr/bin/python3

d = "7d6d6175727d697f4f434c455951485d5658562c2217223a240b3a3f3319060808020819141606"
d = bytes.fromhex(d).decode('utf-8')
d = [ord(i) for i in list(d)]

for k1 in range(255):
    for k2 in range(255):
        m = []
        for i in d:
            m.append(chr(i ^ k1))
            k1 = (k1 + k2) % 255
        m = ''.join(m)
        if "tanggerangkota" in m:
            print("Hasil: ", m)
            break