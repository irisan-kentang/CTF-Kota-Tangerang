## Judul Soal
SequelTime

## Deskripsi Soal

Our system has been compromised again. This time the target were databases

---
## Proof of Concept
- Decode prepared_statement to retrieve bare sql query
- Based on sql query, look for any query execution that has ±0.4-0.5 s time execution
- Found link of both `zip` file and `txt` file
- Decompress zip using given password inside of txt file


## Flag

tangerangkota{t1me_sur3_fli3s_even_f0r_sqli}
