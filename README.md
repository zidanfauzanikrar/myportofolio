Name : Zidan Fauzan Ikrar

NPM : 2506589616

CLass : PBP E


### Week 1

### Instruksi setup:

## 1. Masuk ke folder proyek dan buka terminal
Buka terminal (PowerShell atau Command Prompt) dan masuk ke direktori proyek:
Untuk bash, jalankan `cd myportofolio` di terminal

## 2. Buat Python virtual environment
Jalankan `python -m venv env` di terminal

## 3. Aktifkan virtual environment
Jika menggunakan PowerShell di Windows dan mengalami error Execution Policy, jalankan perintah izin beserta aktivasi berikut di terminal Powershell:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy`
`RemoteSigned .\env\Scripts\Activate.ps1`

## 4. Install dependensi atau library
Jalankan `pip install -r requirements.txt` di terminal

## 5. Migrasikan database
Jalankan `python manage.py migrate` di terminal

## 6. Jalankan server lokal atau buka di Pacil Web Services (PWS)
Untuk server lokal, jalankan `python manage.py runserver` di terminal.
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

* Teknologi Backend (Framework) : Django 5.0
* Dependensi Python : Python 3.13.7
* Perintah Menjalankan Local Server : `python manage.py runserver`
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

1. Ya, saya menggunakan `<section>` untuk mengelompokkan elemen-elemen yang ada di Profile dan di Experience agar lebih mudah diatur saat mengubah tampilan web di style.css. Contohnya bagian `<section id="experience" class="portofolio-section">` di index.html digunakan pada style.css di bagian 

`.portfolio-section {`
`    padding: 5rem 0;`
`    border-top: 1px solid var(--line);`
`}`

untuk memberikan jarak atas dan bawah (padding) serta garis tipis untuk membatasi antar-section portofolio.

2. Saat mengatur kode CSS, masalah tata letak yang saya alami adalah terkait mengatur jarak antarkotak dan membuat header website kelihatan dengan jelas. Masalah jarak antarkotak akhirnya diselesaikan dengan menambahkan `margin-bottom: 1rem` di section `.experience-card`, dan masalah membuat header website kelihatan jelas diselesaikan dengan menambahkan `position: sticky` dan menambahkan shadow pada header tersebut dengan `box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15)` pada `.site-header` agar memiliki garis bayangan tipis sehingga keberadaan header terlihat jelas bahkan saat di-scroll ke bawah. Untuk evaluasi saat berpindah dari tampilan desktop ke mobile, tampilan webnya tetap terlihat jelas dan rapi dikarenakan adanya bagian `@media (max-width: 600px)`.

3. Batasan yang saya rasakan adalah terkait jika ingin menambahkan section yg baru, maka datanya harus di-hardcode di dalam file index.html dan tidak dapat diubah langsung di web. Fungsionalitas dinamis yang ingin saya persiapkan dan tambahkan adalah untuk dapat menambahkan dan mengubah isi informasi portofolio saya terkait pengalaman, proyek, dll bagi pihak tertentu, khususnya saya, pada webnya langsung.


AI Disclosure: 
Menggunakan Gemini Pro 3.1 untuk belajar terkait cara kerja HTML dan CSS serta memberikan panduan terkait bagaimana elemen-elemennya saling berinteraksi dalam kedua file index.html dan style.css dengan contoh kode. Selain itu, AI tersebut juga digunakan untuk memberikan saya ide untuk mendekorasi webnya seperti `box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15)` pada `.site-header` dan garis bawah pada `.section-title::after`.


### Week 2

### Dokumentasi Pembaruan

## 1. Perubahan Struktur Halaman

Portofolio yang sebelumnya satu halaman dengan anchor link (`#profile`, `#experience`) sekarang dipecah menjadi tiga halaman terpisah:
* `index.html` (`main:show_main`) : Bagian Profile/Hero.
* `experience.html` (`main:show_experience`) : Daftar pengalaman, dirender dari `experience_list` lewat `{% for %}`, menampilkan kategori (`get_category_display`), judul, deskripsi, serta status "Ongoing"/"Completed" berdasarkan field `is_ongoing`. Ada fallback teks lewat `{% empty %}` jika belum ada data.
* `skill.html` (`main:show_skill`) : Daftar skill dengan struktur serupa (`skill_list`, kategori, judul, deskripsi).

Navigasi di `.site-header` sekarang mengarah ke masing-masing halaman lewat `{% url %}`, bukan lagi anchor `#profile`/`#experience` seperti di Week 1.

## 2. Penambahan Interaktivitas

* Nav link mendapat garis bawah yang muncul dengan animasi slide-in saat hover (`::after` dengan transisi `width`), dan halaman yang sedang aktif otomatis mendapat garis bawah permanen lewat class `.active`.
* Class `.active` ditambahkan otomatis lewat script baru `static/js/main.js`, yang membandingkan `pathname` tiap link nav dengan `window.location.pathname`.
* Kartu (`.portofolio-card`, dipakai bersama di halaman Experience & Skill) mendapat efek hover: border berubah ke warna aksen dan kartu terangkat sedikit (`transform: translateY`).
* Transisi di atas dinonaktifkan otomatis untuk user dengan preferensi `prefers-reduced-motion: reduce`.

## 3. Perbaikan Bug

* Link Email di bagian Social Links sebelumnya tidak memakai `mailto:` sehingga tidak membuka aplikasi email saat diklik. Sudah diperbaiki menjadi `mailto:zidan.fauzan@ui.ac.id`.

### Tugas 2

1. Browser mengirim request HTTP ke URL (misalnya ke /experience/), request tersebut ditangkap oleh urls.py yang di folder proyek (yaitu portofolio), lalu `include("main.urls)` mengarahkannya ke urls.py yang di dalam main dan pathnya dicocokkan ke view tertentu (misalnya ke `show_experience(request)`), lalu view tersebut memanggil model yang sesuai (misalnya Experience.objects.all()) untuk mengambil data dari database melalui Object-Relational Mapping (ORM), lalu data itu dimasukkan ke dalam dictionary context pada method tersebut dan di-render bersama template experience.html di mana `{{ }}` dan `{{ % for % }}` diubah dengan data aslinya, lalu hasil HTML tersebut dikirim kembali sebagai respons dan browser me-render halamannya menggunakan style.css.

2. Agar data portofolionya dapat lebih mudah diubah dan dikelola, agar ada pemisahan tanggung jawab antara kode-kode dalam templates yang mengelola tampilan dan input data pada web, agar tidak harus mengubah dan men-deploy ulang kode tiap mengubah data portofolio, serta agar struktur dan validasi data lebih rapi dan terjamin.

3. `makemigrations` membuat file migrasi sebagai blueprint skema dari perubahan di models.py, sedangkan `migrate` menerapkan file migrasi tersebut ke database asli. Contoh alurnya yaitu menambah field `is_ongoing = models.BooleanField(default=False)` ke model Experience, lalu `makemigrations` men-generate file migrasi untuk kolom baru tersebut, lalu `migrate` menambahkan kolomnya ke tabel di database.


AI Disclosure:
Menggunakan Claude Sonnet 5.0 High untuk melakukan debugging, contohnya pada link email yang awalnya tidak menggunakan `mailto` agar menyambung ke link dengan semestinya (sekarang menjadi menjadi `mailto:zidan.fauzan@ui.ac.id`). Selain itu, AI tersebut juga digunakan untuk memberikan saya ide-ide terkait penambahan kreativitas tambahan pada tampilan web dan memberikan contoh kodenya untuk saya telusuri dan ubah sesuai kemauan saya. AI tersebut juga saya gunakan untuk mempelajari alur pengiriman dan penerimaan request serta pemindahan data pada proyek ini.



### Week 3

### Dokumentasi Pembaruan

## 1. Template Inheritance (base.html)

Header (navbar) dan footer yang sebelumnya ditulis ulang di tiap halaman sekarang dipusatkan ke satu file `base.html`, memakai `{% block title %}`, `{% block meta %}`, dan `{% block content %}`. Halaman `index.html`, `experience.html`, dan `skill.html` sekarang cukup `{% extends "base.html" %}` dan mengisi block masing-masing, tanpa perlu menulis ulang `<head>`, `<header>`, atau `<footer>`.

## 2. CRUD Penuh untuk Experience & Skill

Sebelumnya cuma ada Create dan Delete untuk Skill. Sekarang kedua entity punya siklus CRUD lengkap:
* `update_experience` dan `update_skill` ditambahkan di `views.py`, memakai form yang sama dengan create (`ExperienceForm`/`SkillForm`) lewat parameter `instance`, dibedakan lewat context `is_edit`.
* Rute `experience/add/`, `experience/<uuid:experience_id>/update/`, dan `experience/<uuid:experience_id>/delete/` didaftarkan di `urls.py` (sebelumnya belum ada sama sekali, jadi fitur create/delete Experience yang sudah ada di `views.py` sebenarnya belum bisa diakses).
* `ExperienceForm` diperluas dengan field `thumbnail` dan `ended_at`, sehingga status ongoing/completed sebuah pengalaman sekarang bisa diatur langsung dari form, bukan cuma otomatis dari `auto_now_add`.
* Template `experience_form.html` dan `skill_form.html` dipakai bersama untuk mode tambah maupun edit.

## 3. Pencarian dan Filter Kategori

Form pencarian pada halaman Experience dan Skill diperluas dengan dropdown filter kategori, mengambil pilihannya langsung dari `EXPERIENCE_CHOICES`/`SKILL_CHOICES` di model (jadi otomatis sinkron kalau kategori baru ditambahkan). Filter judul dan kategori bisa dipakai bersamaan lewat `get_experience_json`/`get_skill_json`.

## 4. Konfirmasi Hapus via Popover API

Tombol Hapus pada tiap kartu Experience dan Skill sekarang memunculkan modal konfirmasi (`experience_delete_modal.html`, `skill_delete_modal.html`) memakai native HTML Popover API (atribut `popover`, `popovertarget`), tanpa JavaScript tambahan untuk buka/tutup modalnya.

## 5. Perbaikan Bug

* Label pada `ExperienceForm` sebelumnya salah salin dari `SkillForm` ("Nama Skill", "Deskripsi Skill", dst), sekarang disesuaikan jadi label Experience.
* Rute create/update/delete untuk Experience belum pernah terdaftar di `urls.py` meski fungsinya sudah ada di `views.py`.
* Template `skill_delete_modal.html` sempat belum ada padahal sudah direferensikan lewat `{% include %}`, sehingga halaman Skill akan gagal render sebelum file ini dibuat.
* Class `.button-danger` belum ada di `style.css` padahal dipakai di kedua modal hapus, sehingga tombol hapus belum berwarna merah seperti seharusnya.
* `CSRF_TRUSTED_ORIGINS` di `settings.py` memakai trailing slash yang menyebabkan error "Origin checking failed" saat deploy ke PWS, karena header Origin dari browser tidak menyertakan slash.

### Tugas 3

1. ModelForm Django digunakan agar menyambung langsung ke model, terdapat validasi otomatis, data form dibersihkan dari input berbahaya, penyimpanan form langsung menyimpan ke database, dan terdapat error handling otomatis. `{% csrf_token %}` wajib ada karena Cross-Site Request Forgery (CSRF) merupakan serangan di mana situs lain membuat request secara tersembunyi menggunakan session user yang sedang login, dan `{% csrf_token %}` menyisipkan token rahasia unik pada form, sehingga setiap kali request POST masuk, Django mencocokannya dengan token yang disimpan pada session user.

2. Karena format JSON lebih ringkas daripada XML, native di JavaScript sehingga lebih mudah untuk frontend, lebih readable, lebih mudah di-debug karena menggunakan tipe data umum, dan parsing lebih mudah dan cepat untuk sebagian besar bahasa.

3. Alur penggunaan view untuk JSON dimulai dengan request yang masuk ke suatu endpoint (misal /api/skills/), ditangkap oleh urls.py, lalu diarahkan ke view get_skill_json. View mengambil data database melalui Object-Relational Mapping menjadi Queryset yang tidak dapat langsung dikirim sebagai HTTP response, sehingga `serializers.serialize("json", skills)` mengubahnya menjadi string JSON. Lalu string JSON tersebut dibungkus menjadi HttpResponse dan dikirim ke client atau view lain seperti `show_skill` dan diserialize lagi untuk digunakan di template.
Serialization di sini dibutuhkan karena HTTP hanya dapat mengirim teks/bytes, sedangkan model Django itu objek kompleks yang memiliki method, relasi ke model lain, dll sehingga tidak memiliki representasi teks bawaan yang sederhana. Namun, serialisasi JSON dapat mengubah model Django tersebut agar dapat dibaca oleh bahasa atau platform manapun karena JSON merupakan format standar.

AI Disclosure: 
Menggunakan Claude Sonnet 5 Effort High untuk membantu menambahkan fungsionalitas update form untuk experience dan skills, untuk debugging dan memastikan konsistensi format antara file-file skills dan experience, untuk membantu menambahkan fungsionalitas tambahan berupa filter pencarian berdasarkan kategori skill atau experience, dan untuk memberikan pemahaman terkait alur perpindahan data dan request pada Django.

Link Log Chat AI: https://claude.ai/share/792c6c31-e28b-4315-96da-7855fab3f149



### Week 4

### Dokumentasi Pembaruan

## 1. Autentikasi dan Sesi

Ditambahkan sistem login penuh, menggunakan komponen bawaan Django:
* `register` memakai `UserCreationForm` untuk membuat akun baru.
* `login_user` memakai `AuthenticationForm`, memanggil `login()` saat kredensial valid, sekaligus menyimpan waktu login ke cookie `last_login`.
* `logout_user` memanggil `logout()` dan menghapus cookie `last_login`.

Kombinasi session bawaan Django dan cookie ini membedakan tiga level akses, pengguna yang belum login, user biasa yang sudah login, dan superuser, yang menentukan tombol dan aksi apa saja yang muncul di tiap halaman.

## 2. Fitur Star/Unstar

Model `Skill` dan `Experience` mendapat field `starred_by`, relasi `ManyToManyField` ke `User`. Fungsi `toggle_skill_star` dan `toggle_experience_star` (dibatasi `@login_required`) menambah atau menghapus user dari relasi itu tergantung status star saat ini, tersedia untuk semua pengguna yang sudah login, tidak dibatasi role tertentu.

## 3. Role Editor lewat Group dan Permission Django

Ditambahkan role baru bernama Editor, dibangun di atas sistem Group dan Permission bawaan Django, bukan field role kustom:
* Data migration membuat Group `Editor`, diberi permission `main.change_skill` dan `main.change_experience` yang otomatis tersedia dari tiap model.
* `update_skill` dan `update_experience` diganti pengecekannya, dari `is_superuser` menjadi `has_perm("main.change_skill")`/`has_perm("main.change_experience")`, sehingga Editor bisa mengedit tanpa perlu jadi superuser.
* `create_skill`, `delete_skill`, `create_experience`, `delete_experience` tetap dikunci khusus superuser.
* Template `skill.html` dan `experience.html` menampilkan tombol Edit berdasarkan `perms.main.change_skill`/`perms.main.change_experience`, terpisah dari tombol Hapus yang tetap dicek lewat `user.is_superuser`, supaya tampilan tombol selalu sinkron dengan apa yang sebenarnya diizinkan di sisi view.

## 4. Halaman 403 Kustom

Error `PermissionDenied` sekarang menampilkan halaman `403.html` yang mewarisi `base.html`, konsisten dengan desain situs. `handler403` diarahkan ke view custom di `views.py` supaya variabel `name` tetap tersedia di navbar dan footer halaman error tersebut.

## 5. Dark Mode Toggle

* Variabel warna di `style.css` direstruktur, sebagian besar sudah memakai CSS custom property sejak awal, ditambah override lewat selector `:root[data-theme="dark"]`.
* Preferensi tema disimpan ke `localStorage`, dibaca lewat script inline di `<head>` sebelum halaman sempat dirender, mencegah kedipan warna saat halaman baru dibuka.
* Tombol toggle ditambahkan di navbar, ikonnya (☀️/🌙) diperbarui otomatis lewat `main.js` mengikuti tema yang aktif.

## 6. Perbaikan Bug

* Pesan dari `messages` framework (misalnya "Skill berhasil diperbarui!") sempat nyangkut dan muncul di halaman yang tidak relevan, seperti halaman Login, karena hanya `login.html` yang merender blok `{% for message in messages %}`. Blok render pesan dipindah ke `base.html` supaya berlaku otomatis di semua halaman tujuan redirect.
* Tombol star/unstar nyaris tidak terlihat saat dark mode aktif, karena `.button-star` memakai `background: var(--ink)`, variabel yang nilainya berbalik terang di tema gelap, sementara teksnya tetap putih. Diganti ke `var(--neutral)`, warna abu gelap yang nilainya tidak berubah mengikuti tema, mengikuti pola yang sama dengan `.button-secondary`.
* Data terkait user dengan daftar username yang telah memberikan bintang pada suatu skill/experience dapat diakses oleh siapa pun pada `/api/skills` dan `/api/experience`, field `starred_by` sekarang dibatasi pada `get_skill_json` dan `get_experience_json` agar tidak membocorkan data yang mungkin bersifat sensitif berupa daftar username tersebut.

AI Disclosure: 
Menggunakan Claude Sonnet 5 Extra Effort untuk membantu menambahkan model `create_editor_group` dan mempelajari alur validasi mengenai masing-masing role (user sudah login, guest, superuser, dan terutama role yang harus dibuat sendiri seperti editor). Selain itu, AI tersebut juga digunakan untuk membantu menerapkan dark mode toggle sebagai fungsionalitas tambahan week ini beserta halaman 403 yang customized. AI tersebut juga digunakan untuk perbaikan bug seperti messages yang muncul secara tak terduga pada halaman login, memperbaiki warna pada kode css agar semuanya menggunakan variabel agar mudah diubah ke dark mode, dan memastikan endpoint JSON tidak membocorkan data sensitif.

Link Log Chat AI: https://claude.ai/share/792c6c31-e28b-4315-96da-7855fab3f149