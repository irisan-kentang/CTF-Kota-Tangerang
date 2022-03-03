## Judul Soal
Ranger

## Deskripsi Soal

A suspicious request detected in our network. It was suspected that the perpetrator tried to download something in the process. Could you investigate what is it?

---
## Proof of Concept
- TLS decryption using `cert.key`, got HTTP request
- Extract partial HTTP request of flag.zip by mapping its content with `range-bytes` header

## Flag

tangerangkota{r4nge_byt3s_p4rtial_requ3st_f0r_fun}
