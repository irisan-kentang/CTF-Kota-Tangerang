## Judul Soal
Fraud

## Deskripsi Soal

Apparently around this year, we'd received a numerous reports of phishing activities. It can be said that it was a classic-type of phishing type which is mainly targetting social media user. Recently, we found that a Twitter user named `J5ggR` that might be the real perpretator. Also he seems to host his code in a certain repository. Could you provide us with some details?

1. What is the perpretator's real name? (eg: John Smith)
2. What is the perpreator's platform target (eg: Reddit)
3. Where is the location (city) of perpretator's server? (eg: New York)

format: `tangerangkota{Name_Platform_City}`
eg: tangerangkota{JohnSmith_Reddit_NewYork}

---
## Proof of Concept
- Make use of `Twitter forgot password`, found `vi******@p****`
- User lookup using `vi in:email` & `created:>2022-01-01`, found `Vivien Nikola` as suspected user
- Check core.db for `server detail`, then IP lookup to obtain `server location`
- Check repository name for `phishing platform`

## Flag

tangerangkota{VivienNikola_Facebook_Tokyo}
