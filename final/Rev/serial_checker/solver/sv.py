from pwn import *
from z3 import *

s = Solver()
ss = [Int('ss%s' % (i)) for i in range(29)]

s.add(ss[9] - ss[7] + ss[27]  == 78)
s.add(ss[25] - ss[21]  == 12)
s.add(ss[8] - ss[27] * ss[21]  == -5539)
s.add(ss[22] % ss[28] + ss[27]  == 80)
s.add(ss[25] % ss[1]  == 12)
s.add(ss[25] % ss[17]  == 42)
s.add(ss[27] + ss[24] - ss[22]  == 63)
s.add(ss[7] % ss[10]  == 83)
s.add(ss[13] - ss[5]  == 23)
s.add(ss[22] * ss[22]  == 7396)
s.add(ss[10] - ss[2] * ss[2]  == -4140)
s.add(ss[2] % ss[2]  == 0)
s.add(ss[25] % ss[2]  == 22)
s.add(ss[23] - ss[25]  == -42)
s.add(ss[20] - ss[26] - ss[1]  == -58)
s.add(ss[28] + ss[10]  == 166)
s.add(ss[25] - ss[12]  == 9)
s.add(ss[22] - ss[28] % ss[26]  == 74)
s.add(ss[1] % ss[4]  == 75)
s.add(ss[28] % ss[6] + ss[3]  == 163)
s.add(ss[7] % ss[6]  == 0)
s.add(ss[25] - ss[12]  == 9)
s.add(ss[3] * ss[15]  == 5412)
s.add(ss[9] % ss[14]  == 4)
s.add(ss[7] + ss[5] * ss[0]  == 3953)
s.add(ss[18] - ss[6]  == -7)
s.add(ss[8] + ss[2]  == 151)
s.add(ss[28] % ss[20] + ss[9]  == 167)
s.add(ss[8] - ss[14]  == 4)
s.add(ss[8] - ss[7]  == 3)
s.add(ss[22] * ss[20]  == 7396)
s.add(ss[13] + ss[24]  == 142)
s.add(ss[4] * ss[16]  == 5893)
s.add(ss[25] - ss[28] + ss[21]  == 81)
s.add(ss[17] * ss[10]  == 3825)
s.add(ss[18] - ss[16]  == 5)
s.add(ss[23] % ss[25]  == 45)
s.add(ss[21] + ss[5] % ss[16]  == 120)
s.add(ss[10] + ss[8]  == 171)
s.add(ss[19] % ss[10] + ss[17]  == 124)
s.add(ss[17] + ss[0] % ss[26]  == 62)
s.add(ss[0] * ss[14] + ss[3]  == 7134)
s.add(ss[4] * ss[8]  == 7138)
s.add(ss[23] - ss[0] % ss[27]  == 34)
s.add(ss[26] - ss[1] * ss[10]  == -6306)
s.add(ss[21] - ss[21]  == 0)
s.add(ss[16] - ss[7] * ss[19]  == -6486)
s.add(ss[26] + ss[22] - ss[22]  == 69)
s.add(ss[2] + ss[0]  == 151)
s.add(ss[10] % ss[10]  == 0)
s.add(ss[19] - ss[20] * ss[14]  == -6973)
s.add(ss[27] - ss[5] - ss[22]  == -56)
s.add(ss[9] - ss[6]  == 3)
s.add(ss[2] + ss[27] + ss[6]  == 223)
s.add(ss[25] % ss[23] - ss[8]  == -44)
s.add(ss[7] + ss[0] % ss[17]  == 124)
s.add(ss[15] - ss[17]  == 21)
s.add(ss[22] % ss[13]  == 18)
s.add(ss[20] - ss[7]  == 3)
s.add(ss[23] * ss[25]  == 3915)
s.add(ss[8] * ss[15] + ss[12]  == 5754)
s.add(ss[21] % ss[1]  == 0)
s.add(ss[19] % ss[15]  == 13)
s.add(ss[6] + ss[24]  == 157)
s.add(ss[7] - ss[25] % ss[26]  == 65)
s.add(ss[22] + ss[21] + ss[8]  == 247)
s.add(ss[24] % ss[18] + ss[17]  == 119)
s.add(ss[24] + ss[5]  == 119)
s.add(ss[13] % ss[26]  == 68)
s.add(ss[17] + ss[8]  == 131)
s.add(ss[9] - ss[1]  == 11)
s.add(ss[28] + ss[27]  == 156)
s.add(ss[12] % ss[19]  == 78)
s.add(ss[28] - ss[8] % ss[1]  == 70)
s.add(ss[14] % ss[21]  == 7)
s.add(ss[4] - ss[14] - ss[17]  == -44)
s.add(ss[26] * ss[12]  == 5382)
s.add(ss[15] * ss[8] * ss[23]  == 255420)
s.add(ss[17] + ss[13] % ss[10]  == 113)
s.add(ss[25] % ss[27] - ss[3]  == -70)
s.add(ss[18] % ss[18]  == 0)
s.add(ss[25] - ss[15]  == 21)
s.add(ss[7] * ss[6]  == 6889)
s.add(ss[2] + ss[15]  == 131)
s.add(ss[24] * ss[6] * ss[19]  == 485218)
s.add(ss[0] + ss[9]  == 172)
s.add(ss[23] % ss[26] % ss[9]  == 45)
s.add(ss[6] + ss[17] - ss[8]  == 42)
s.add(ss[0] % ss[17] * ss[28]  == 3321)
s.add(ss[18] + ss[2]  == 141)
s.add(ss[14] * ss[27]  == 6150)
s.add(ss[25] + ss[0]  == 173)
s.add(ss[18] * ss[21]  == 5700)
s.add(ss[12] - ss[8]  == -8)
s.add(ss[20] + ss[11] % ss[14]  == 131)

r = remote('localhost', 30001)

if s.check() == sat:
    m = s.model()
    ans = ''

    for c in ss:
        ans += chr(abs(m[c].as_long()))

    r.sendline(ans)
    print(r.recvall())
