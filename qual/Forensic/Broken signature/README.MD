## Judul Soal
Broken signature

## Deskripsi Soal

I hid the flag inside the image's comment. Unfortunately, it was corrupted by accident.

---
## Proof of Concept
- Repair PNG signature by changing `CTF` into `PNG`
- Look for `Comment` in Exif-data to obtain the flag 

## Flag

tangerangkota{th4nks_for_rec0v3ring_me}