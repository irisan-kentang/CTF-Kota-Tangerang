## Judul Soal
cryptor

## Deskripsi Soal
just a dummy encryptor..

---
## Proof of Concept
- Given `flag.txt.enc`, `cryptor` binary, and libc `libc-2.3.1.so`
- We found that there's a random seed initialization of current_time at the beginning of program. Thus we can make use of `modified_time` of `flag.txt.enc` to obtain the right seed.
- Apply `libc-2.3.1.so` using python CDLL module in order to simulate the random & encryption function 

## Flag

tangerangkota{s1mpl3__yet__dummy_fil3_3ncryptor}
