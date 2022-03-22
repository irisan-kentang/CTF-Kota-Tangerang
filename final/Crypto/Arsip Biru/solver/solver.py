import base64

# plain = aaaaaaaaaaa|name=a
# result = name=aaaaaaaaaaa|name=a|sensei=0
encrypted = "0AtMCdr2UXGSfwiexul+H0v503WvLxcPHHya8wsUOkXQJJuMa+fOJl5+lvnvKAJz"
encrypted = base64.b64decode(encrypted)

n = 16
blocks = [encrypted[i:i+n] for i in range(0, len(encrypted), n)]
block = blocks[0]

blocklist = list(block)
blocklist[15] = block[15] ^ ord('0') ^ ord('1')
block = bytes(blocklist)
blocks[0] = block

encrypted = blocks[0] + blocks[1] + blocks[2]
encrypted = base64.b64encode(encrypted)

print(encrypted)
# 0AtMCdr2UXGSfwiexul+Hkv503WvLxcPHHya8wsUOkXQJJuMa+fOJl5+lvnvKAJz