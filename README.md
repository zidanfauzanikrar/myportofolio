Name : Zidan Fauzan Ikrar

NPM : 2506589616

CLass : PBP E


### Instruksi setup:

## 1. Masuk ke folder proyek dan buka terminal
Buka terminal (PowerShell atau Command Prompt) dan masuk ke direktori proyek:
Untuk bash, jalankan ```cd myportofolio``` di terminal

## 2. Buat Python virtual environment
Jalankan ```python -m venv env``` di terminal

## 3. Aktifkan virtual environment
Jika menggunakan PowerShell di Windows dan mengalami error Execution Policy, jalankan perintah izin beserta aktivasi berikut di terminal Powershell:
```Set-ExecutionPolicy -Scope Process -ExecutionPolicy```
```RemoteSigned .\env\Scripts\Activate.ps1```

## 4. Install dependensi atau library
Jalankan ```pip install -r requirements.txt``` di terminal

## 5. Migrasikan database
Jalankan ```python manage.py migrate``` di terminal

## 6. Jalankan server lokal atau buka di Pacil Web Services (PWS)
Untuk server lokal, jalankan ```python manage.py runserver``` di terminal.
Lalu akses situs webnya di browser melalui alamat http://127.0.0.1:8000/


### Dokumentasi:

## 1. Ringkasan Proyek

Situs web ini merupakan portofolio pribadi untuk Zidan Fauzan Ikrar, mahasiswa S1 Ilmu Komputer Universitas Indonesia. Situs ini mengandung profil singkat, link media sosial, dan daftar pengalaman akademik serta mengajarnya.

## 2. Struktur Halaman (index.html)

Halaman web terbagi menjadi beberapa bagian utama:
* Header & Navigasi (`.site-header`) :
    * Menampilkan nama pemilik portofolio ("Zidan Fauzan Ikrar").
    * Menyediakan menu navigasi cepat menuju bagian Profile (`#profile`) dan Experience (`#experience`).

* Hero / Bagian Profil (`#profile`) :
    * Identitas : Menampilkan status program studi di Universitas Indonesia.
    * Foto : Menampilkan foto profil avatar dari direktori `/static/img/zidanfauzanikrar.jpeg`.
    * Detail Profil : Mengandung deskripsi singkat (fokus pada Machine Learning & AI), NPM (`2506589616`), dan Program Studi (`S1 Ilmu Komputer`).
    * Link Media Sosial : Menyediakan link GitHub, LinkedIn, dan kontak Email (`zidan.fauzan@ui.ac.id`).

* Bagian Pengalaman (`#experience`) :
    * Memuat judul bagian Experience.
    * Mengajar UTBK : Pengalaman sebagai pengajar subtes Penalaran Umum (PU) di BETIS Fasilkom UI.
    * Mengajar Pemrograman : Pengalaman sebagai mentor DDP0 Fasilkom UI untuk materi Python.
    * Menjadi Asisten Dosen : Pengalaman menyiapkan tutorial, mengawas, dan mengoreksi kuis mata kuliah Logika dan Struktur Diskret.

* Footer (`.site-footer`) :
    * Menampilkan catatan hak cipta tahun 2026 untuk Zidan Fauzan Ikrar, Fakultas Ilmu Komputer, Universitas Indonesia.

## 3. Spesifikasi Desain & Gaya (style.css)

* Sistem Warna (`:root`) :
    * Latar Belakang (`--paper`): `#faf6f0`
    * Teks Utama (`--ink`): `#1c1917`
    * Warna Aksen Utama (`--accent`): `#d95d39`
    * Warna Aksen Gelap (`--accent-dark`): `#a8442a`
    * Warna Aksen Terang / Kartu (`--accent-light`): `#ffd7b2`
    * Garis Pembatas (`--line`): `#e3d9c9`
    * Warna Teks Sekunder (`--text-muted`, `--text-less-muted`): `#6b6459` dan `#4b4439`

* Tipografi :
    * Menggunakan font Space Grotesk untuk nama brand dan judul utama (`h1`, `.section-title`).
    * Menggunakan font sistem (sans-serif) untuk teks paragraf biasa.

* Komponen & Interaktivitas UI :
    * Header Menempel (Sticky Header) : Menempel di bagian atas layar (`position: sticky`) dengan efek bayangan bawah (`box-shadow`) saat di-scroll.
    * Efek Hover : Navigasi dan brand berubah warna menjadi `--accent` saat kursor mendekati teks.
    * Tata Letak Grid Hero : Tampilan 2 kolom pada desktop otomatis berubah menjadi 1 kolom pada tampilan mobile (`max-width: 600px`).
    * Garis Aksen Judul : Judul bagian `.section-title` dilengkapi garis hiasan di bawah teks menggunakan `::after` bertema warna aksen.
    * Kartu Pengalaman (`.experience-card`) : Memiliki latar belakang berwarna `--accent-light`, sudut melengkung (`--radius`), dan garis tepi `border: 2px solid var(--line)`.

## 4. Informasi Environment & Instalasi

* Teknologi Backend (Framework) : Django 6.1
* Dependensi Python : Python 3.13.7
* Perintah Menjalankan Local Server : ```python manage.py runserver```
* Link Deployment PWS : zidan-fauzan-myportofolio.pws.cs.ui.ac.id
* Dependensi lain:
    * asgiref==3.12.1
    * certifi==2026.7.22
    * charset-normalizer==3.5.1
    * gunicorn==26.2.0
    * idna==3.19
    * psycopg2-binary==2.9.12
    * python-dotenv==1.2.3
    * requests==2.34.2
    * sqlparse==0.6.0
    * tzdata==2026.3
    * urllib3==2.7.0
    * whitenoise==6.12.0*


### Tugas 1

1. Ya, saya menggunakan ```<section>``` untuk mengelompokkan elemen-elemen yang ada di Profile dan di Experience agar lebih mudah diatur saat mengubah tampilan web di style.css. Contohnya bagian ```<section id="experience" class="portofolio-section">``` di index.html digunakan pada style.css di bagian 

```.portfolio-section {```
```    padding: 5rem 0;```
```    border-top: 1px solid var(--line);```
```}```

untuk memberikan jarak atas dan bawah (padding) serta garis tipis untuk membatasi antar-section portofolio.

2. Saat mengatur kode CSS, masalah tata letak yang saya alami adalah terkait mengatur jarak antarkotak dan membuat header website kelihatan dengan jelas. Masalah jarak antarkotak akhirnya diselesaikan dengan menambahkan ```margin-bottom: 1rem``` di section ```.experience-card```, dan masalah membuat header website kelihatan jelas diselesaikan dengan menambahkan ```position: sticky``` dan menambahkan shadow pada header tersebut dengan ```box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15)``` pada ```.site-header``` agar memiliki garis bayangan tipis sehingga keberadaan header terlihat jelas bahkan saat di-scroll ke bawah. Untuk evaluasi saat berpindah dari tampilan desktop ke mobile, tampilan webnya tetap terlihat jelas dan rapi dikarenakan adanya bagian ```@media (max-width: 600px)```.

3. Batasan yang saya rasakan adalah terkait jika ingin menambahkan section yg baru, maka datanya harus di-hardcode di dalam file index.html dan tidak dapat diubah langsung di web. Fungsionalitas dinamis yang ingin saya persiapkan dan tambahkan adalah untuk dapat menambahkan dan mengubah isi informasi portofolio saya terkait pengalaman, proyek, dll bagi pihak tertentu, khususnya saya, pada webnya langsung.


AI Disclosure: 
Menggunakan Gemini Pro 3.1 untuk belajar terkait cara kerja HTML dan CSS serta memberikan panduan terkait bagaimana elemen-elemennya saling berinteraksi dalam kedua file index.html dan style.css dengan contoh kode. Selain itu, AI tersebut juga digunakan untuk memberikan saya ide untuk mendekorasi webnya seperti ```box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15)``` pada ```.site-header``` dan garis bawah pada ```.section-title::after```.