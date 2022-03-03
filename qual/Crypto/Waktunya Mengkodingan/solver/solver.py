#!/usr/bin/python3

d = "7d6d6175706a7a70464f485e4c4b58595d5551251a213f3b0e39323424050d07070b04131b05"
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