#!/usr/bin/python2
from pwn import *
from ctypes import CDLL
from string import digits, letters

import os

enc = open('flag.txt.enc', 'rb').read()
mtime = int(os.stat('flag.txt.enc').st_mtime)

libc = CDLL('libc-2.31.so')
libc.srand(mtime)

def make_key(length=8):
    charset = digits + letters
    RAND_MAX = 2147483647.0

    return bytearray(
        charset[int(libc.rand()/RAND_MAX*62)] \
        for x in range(8)
    )

flag = ''
for x in range(0, len(enc), 8):
    key = make_key()
    current = enc[x:x+8]

    if not x:
        flag += xor(current, key)
    else:
        flag += xor(xor(prev, current), key)

    prev = current

print(flag.strip())