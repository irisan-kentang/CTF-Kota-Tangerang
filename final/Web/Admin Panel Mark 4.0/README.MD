## Judul Soal
Admin Panel

## Deskripsi Soal
apa yang diharapkan dari admin panel? ya hanya admin yang dapat login :)

---

## Penjelasan Penyelesaian Soal
- Terdapat kolom `role` pada model di array `$fillable`, artinya bisa diinput menggunakan mass insert
- Pada kode registrasi di controller, ternyata menggunakan mass insert untuk semua request
- Override role pada form pendaftaran menjadi admin (via inspect element)
- `<input type="text" name="role" value="admin">`

## FLAG
tangerangkota{always_check_your_model_and_request}
