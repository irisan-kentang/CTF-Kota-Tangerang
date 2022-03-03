## Judul Soal
Admin Panel

## Deskripsi Soal
apa yang diharapkan dari admin panel? ya hanya admin yang dapat login :)

---

## Penjelasan Penyelesaian Soal
- Bypass login menggunakan SQL Injection teknik union
- Mencoba memasukan tanda petik akan mengakibatkan error
- Pertama, perlu mencari jumlah kolom dengan payload `' union select 1, 1, 1, 1` dengan memasukkan password 1
- Setelah mengetahui jumlah kolom, kita asumsikan role ada pada kolom ke 4, jadi kita ubah payload menjadi
- `' union select 1, 1, 1, 'admin' -- -` dengan password tetap 1

## FLAG
tangerangkota{hekel_hekel_es_ki_el}