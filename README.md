# Dashboard

## Tujuan:
1. Menampilkan data yang didapat dari sistem altmetrik
2. 

**Daftar isi:**
- [Dashboard](#dashboard)
  * [Tujuan:](#tujuan)
  * [Requirement:](#requirement)
  * [Cara Installasi:](#cara-installasi)
  * [Penjelasan Dashboard](#penjelasan-dashboard)

### Requirement:
----
1. Bokeh library
2. Web framework Django

### Cara Installasi:
----
1. Install Python
2. Install Django menggunakan pip di command prompt (...\>pip install Django)
3. Mulai projek dengan startproject ($ django-admin startproject mysite)
4. Mulai server dengan ($ manage.py runserver)

### Penjelasan Dashboard                
----
1. Halaman Depan
Halaman depan berisi penjelasan umum semua dokumen, berisikan jumlah dokumen, grafik jenis dokumen, bahasa dokumen, dan lain lain.
2. Detail-1
Halaman detail-1 berisi id dan nama lengkap dokumen
3. Detail-2
Halaman detail-2 berisi data rincian setiap dokumen yang didapat dari altmetrik.
