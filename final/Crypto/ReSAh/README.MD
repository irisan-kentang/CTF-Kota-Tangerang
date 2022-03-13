## Judul Soal
ReSAh

## Deskripsi Soal

Simple RSA
---
## Proof of Concept

- cari p dan q di factordb
```py
from Crypto.Util.number import inverse

n = 245841236512478852752909734912575581815967630033049838269083
p = 416064700201658306196320137931
q = 590872612825179551336102196593
e = 65537
c = 137333426733196481216501577154747463257382613151317418707134

phi = (p-1)*(q-1)
d = inverse(e, phi)

m = pow(c, d, n)
print(bytes.fromhex(hex(m)[2:]))
```

## Flag

tangerangkota{rsa_gaming_goes_brr}