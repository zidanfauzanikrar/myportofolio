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



### Week 5

### Dokumentasi Pembaruan

## 1. Menampilkan Data dengan AJAX

Halaman `experience.html` dan `skill.html` diubah dari render server-side penuh menjadi kerangka halaman saja. `show_experience`/`show_skill` tidak lagi mengirim `experience_list`/`skill_list`, hanya `title_query`, `category_query`, `category_choices`, dan `form` (untuk modal tambah data). Data daftar diambil lewat `fetch()` ke `get_experience_json`/`get_skill_json`, yang sekarang membangun JSON secara manual (bukan `serializers.serialize`), menyertakan `category_display`, `is_ongoing`, `star_count`, dan `is_starred` per item, dihitung dari sisi server memakai `annotate(Count("starred_by"))` supaya tidak membuka query terpisah per item.

Empat kondisi ditangani lewat elemen `#loading`, `#error`, `#empty`, `#grid`, ditoggle lewat class `.hide` yang baru ditambahkan ke `style.css`.

## 2. Pencarian dengan Debouncing dan Filter Kategori

Input pencarian memicu `fetch()` setelah jeda 300ms dari ketikan terakhir (`setTimeout`/`clearTimeout`), bukan menunggu submit form. Dropdown kategori memicu pencarian langsung saat `change`. `AbortController` dipakai untuk membatalkan request sebelumnya kalau ada request baru, mencegah hasil yang lebih lama menimpa hasil yang lebih baru.

## 3. Menambahkan Data lewat Modal dan AJAX

Form tambah Experience/Skill dipindah ke dalam modal (Popover API), dipisah jadi `components/experience_modal_form.html` dan `components/skill_modal_form.html`, di-include setelah `</main>`, dibungkus `{% if user.is_superuser %}`. Endpoint baru `create_experience_ajax`/`create_skill_ajax` dibuat khusus untuk alur ini, memeriksa `is_authenticated`/`is_superuser` secara manual (bukan `@login_required`) supaya semua jalur keluar tetap membalas JSON dengan status yang sesuai (201 berhasil, 400 validasi gagal, 403 tidak berizin, 405 method salah). Token CSRF dikirim lewat header `X-CSRFToken`, dibaca dari cookie `csrftoken` lewat `getCookie()`. Setelah berhasil, daftar di-refresh lewat `fetchExperiences()`/`fetchSkills()` tanpa reload halaman.

## 4. Notifikasi Toast

Komponen toast tunggal (`components/toast.html`, di-include sekali di `base.html`) dikendalikan `toast.js`, memakai `popover="manual"` supaya tidak ikut mekanisme light-dismiss otomatis dan tidak saling menutup dengan modal lain yang sedang terbuka. Dipanggil lewat `showToast(title, message, type)` setelah tambah data berhasil maupun gagal, termasuk menampilkan pesan validasi dari server.

## 5. Perlindungan XSS

Di sisi client, semua teks dinamis (`title`, `description`, dst) yang disisipkan lewat `innerHTML` saat membangun kartu dilewatkan ke `escapeHtml()` terlebih dahulu. Di sisi server, `ExperienceForm` dan `SkillForm` mendapat method `clean_title`, `clean_description`, `clean_category` yang memakai `strip_tags`, dengan validasi tambahan di `clean_title` agar input yang isinya cuma tag HTML (jadi kosong setelah dibersihkan) ditolak sebagai error, bukan tersimpan sebagai string kosong.

## 6. Perbaikan Bug

* `experience.tech_stack`, sisa dari tutorial Project, direferensikan padahal `Experience` tidak punya field itu, diganti ke `experience.category`.
* `starred_by_names` (daftar username yang memberi star) dihapus dari kedua endpoint JSON, mengulang kebocoran privasi yang sebelumnya sudah ditutup, diganti cukup dengan `star_count`.
* `category_display` dan `is_ongoing` sempat tidak ikut dikirim di JSON, menyebabkan label kategori kosong dan semua experience tampil "Completed" apa pun status aslinya.
* `category_query`, `category_choices`, dan `form` sempat tidak dikirim dari `show_experience`/`show_skill`, menyebabkan dropdown kategori tidak terisi dan modal tambah data terbuka tanpa field apa pun.
* Pesan error dari modal tambah data digabung jadi satu string tanpa nama field, membuat pesan seperti "This field is required." muncul berulang tanpa keterangan field mana yang dimaksud.
* Field `category` pada form masih memakai `TextInput` dengan placeholder berisi label tampilan, padahal validasi membandingkan ke value asli (`programming_language`, dst), menyebabkan error "not one of the available choices" saat user mengetik sesuai placeholder. Diperbaiki dengan mengembalikan ke `<select>` bawaan Django (menghapus override widget tersebut).
* `.toast-success` di `style.css` sempat punya `border-left: 4px solid ;` tanpa warna, membuat toast sukses tidak bergaris warna seperti toast error/normal, diperbaiki memakai variabel `--safe` yang sudah didefinisikan tapi belum terpakai.

## 7. Fitur Tambahan: Filter "Starred by Me"

Halaman Experience dan Skill mendapat checkbox "Starred by me" yang hanya muncul untuk pengguna yang sudah login. Saat dicentang, daftar hanya menampilkan item yang sudah diberi star oleh pengguna tersebut. Filter ini bisa dikombinasikan dengan pencarian judul dan filter kategori, dan berjalan tanpa reload halaman.

* Frontend: checkbox `#starred-filter` ditambahkan ke form pencarian. Perubahannya memicu `fetch()` dengan parameter `starred=1`. Status awalnya dibaca dari query string lewat context `starred_query`, dan elemennya tidak dirender untuk pengunjung anonim.
* Backend: `get_experience_json` dan `get_skill_json` membaca parameter `starred` dan memfilter dengan `pk__in` terhadap himpunan id item yang di-star pengguna saat ini. Memfilter langsung dengan `filter(starred_by=request.user)` akan membatasi join yang dipakai `annotate(Count("starred_by"))`, sehingga `star_count` salah menjadi 1 untuk setiap item.
* Keamanan: pengguna anonim tidak punya himpunan star, sehingga `starred=1` yang dikirim manual lewat URL menghasilkan daftar kosong. Respons tetap tidak memuat daftar username pemberi star.
* Keterbatasan: tombol star masih memakai POST biasa dengan redirect, sehingga setelah star/unstar halaman dimuat ulang dan status filter kembali ke default. Mengubah star menjadi AJAX akan menyelesaikan hal ini.

### Tugas 5

1. Debouncing merupakan teknik menunda eksekusi suatu fungsi hingga jeda waktu tertentu berlalu sejak terakhir kali fungsi itu dipicu. Jika fungsi tersebut dipicu lagi sebelum jeda waktunya habis, maka timer sebelumnnya dibatalkan dan dihitung ulang dari awal. Ini menyebabkan fungsi baru benar-benar jalan setelah user berhenti memicu event baru untuk sementara waktu. Debouncing penting untuk pencarian AJAX agar mengurangi beban server, mencegah race conditon pada hasil, dan memberikan pengalaman yang lebih hemat baterai dan data untuk pengguna.

2. `fetch()` merupakan fungsi asinkronus, jadi saat dipanggil, ia akan mengembalikan objek Promise yang tidak mengandung respons langsung karena request ke server membutuhkan waktu dan JavaScript tidak akan berdiam untuk menunggu request tersebut selesai. `await` di depan `fetch()` memberikan jeda eksekusi fungsi `async` yang memanggilnya hingga Promise itu selesai, lalu nilai response aslinya akan dikembalikan dan baris kode berikutnya dijalankan.

3. Cross-Site Scripting (XSS) merupakan serangan di mana penyerang menyisipkan kode JavaScript berbahaya ke dalam halaman web, yang kemudian dijalankan di browser pengguna lain yang sedang membuka halaman tersebut, seolah-olah kode tersebut bagian asli dari situsnya. Melalui XSS, penyerang dapat mencuri cookie session, mengambil alih akun, mengirim request atas nama korban, atau mengubah tampilan halaman secara tersembunyi. Data melalui AJAX atau JS lebih rentan dibandingkan template Django biasa karena Django template memiliki auto-escaping bawaan yang mengubah karakter berbahaya menjadi entitas HTML sebelum dikirim ke browser, sedangkan data melalui JsonResponse tidak melalui mesin template Django dan innerHTML di JavaScript tidak melakukan escaping apapun.

AI Disclosure: 
Menggunakan Claude Sonnet 5.5 High untuk memberikan penyesuaian kode Tutorial terutama pada implementasi penyesuaian AJAX pada kode saya, membantu mencari dan membenarkan bug pada kode saya terutama pada notifikasi Toast yang terlihat aneh, membantu memberikan pemahaman lebih lanjut terkait materi minggu ini, serta membantu memberikan ide dan mengimplementasikan fitur tambahan untuk minggu ini.

Link Log Chat AI: https://claude.ai/share/792c6c31-e28b-4315-96da-7855fab3f149



### Week 6

### Dokumentasi Pembaruan

## 1. REST API dengan Django REST Framework

Endpoint JSON buatan sendiri (`get_experience_json`, `get_skill_json`, `create_experience_ajax`, `create_skill_ajax`) digantikan oleh API berbasis Django REST Framework untuk model `Experience` dan `Skill`. Halaman Experience dan Skill tidak lagi memakai endpoint lama tersebut.

* `serializers.py` : `SkillSerializer` dan `ExperienceSerializer` berbagi satu mixin (`PortfolioItemMixin`) yang berisi validasi teks (`strip_tags`, judul/deskripsi tidak boleh kosong setelah dibersihkan) serta field hitungan `star_count` dan `is_starred`. Kedua field itu read-only dan dihitung dari `annotate()` sehingga jumlah query tetap konstan berapa pun jumlah itemnya. Daftar username pemberi star tidak pernah dikirim.
* `api_views.py` : memakai `@api_view` dengan `SessionAuthentication`. Daftar mendukung filter `?title=`, `?category=`, dan `?starred=1`. Pembuatan data membalas 201, validasi gagal membalas 400, tidak berizin membalas 403, dan id tidak ditemukan membalas 404.
* `api_urls.py` : didaftarkan di `urls.py` proyek lewat `path("api/v1/", include("main.api_urls"))` dengan namespace `api`, ditambah `api-auth/` untuk login di Browsable API.

| Endpoint | Method | Fungsi |
| --- | --- | --- |
| `/api/v1/skills/` dan `/api/v1/experience/` | GET, POST | Daftar (dengan filter) dan tambah data |
| `/api/v1/skills/<uuid>/` dan `/api/v1/experience/<uuid>/` | GET, PUT, PATCH, DELETE | Detail, ubah (penuh atau sebagian), hapus |
| `/api/v1/skills/<uuid>/star/` dan `/api/v1/experience/<uuid>/star/` | POST | Star/unstar, membalas item terbaru |

## 2. Izin Akses Berbasis Peran

Izin tulis dicek lewat `permissions.py`. `IsPortfolioOwnerOrReadOnly` dipakai pada endpoint daftar (POST hanya superuser). `IsPortfolioOwnerOrEditorOrReadOnly(Model)` dipakai pada endpoint detail dan memeriksa Permission Django lewat `has_perm` (`change_*` untuk PUT/PATCH, `add_*` untuk POST, `delete_*` untuk DELETE), bukan nama Group, sehingga mencabut izin di admin langsung mencabut aksesnya. Endpoint star memakai `IsAuthenticated`.

| Peran | Baca | Star | PUT/PATCH | POST | DELETE |
| --- | --- | --- | --- | --- | --- |
| Pengunjung (belum login) | Ya | Tidak | Tidak | Tidak | Tidak |
| Pengguna biasa | Ya | Ya | Tidak | Tidak | Tidak |
| Editor | Ya | Ya | Ya | Tidak | Tidak |
| Pemilik (superuser) | Ya | Ya | Ya | Ya | Ya |

Catatan: ini izin berbasis peran untuk satu portofolio. Permission per-view tidak menyaring objek milik pengguna lain, jadi jika kelak ada banyak pemilik dan data privat, pemeriksaan objek dan pembatasan queryset perlu didesain tersendiri. Karena memakai `SessionAuthentication`, setiap request tulis dari pengguna yang login wajib menyertakan token CSRF.

## 3. Pembaruan Frontend

Script di `experience.html` dan `skill.html` disesuaikan dengan kontrak data baru.

* Data item sekarang flat (`item.id`, `item.title`, ...), bukan `item.pk` dan `item.fields`. Endpoint dibaca lewat `{% url 'api:...' %}`.
* Semua request tulis melewati satu fungsi `sendApi()` yang mengirim JSON dengan header `X-CSRFToken`. Error DRF (`{field: [pesan]}` maupun `{detail: ...}`) diubah menjadi pesan yang ditampilkan lewat toast, termasuk pesan saat server tidak terjangkau.
* Edit lewat modal: tombol Edit membuka modal (`components/experience_edit_modal.html`, `components/skill_edit_modal.html`) yang terisi data kartu, lalu mengirim `PATCH` ke endpoint detail. Form edit memakai `auto_id="id_edit_%s"` agar ID inputnya tidak bentrok dengan form tambah.
* Star lewat AJAX: tombol memanggil endpoint `/star/`, kartu diganti di tempat tanpa reload halaman. Jika filter "Starred by me" aktif, daftar dimuat ulang agar kartu yang di-unstar hilang.
* Hapus lewat AJAX: tombol "Ya, Hapus" pada modal konfirmasi memanggil `DELETE`. Tombol Hapus kini mengikuti izin `perms.main.delete_*`, bukan lagi `user.is_superuser`, sehingga Editor tidak melihatnya.
* Tambah data memakai `POST` JSON ke API (bukan lagi FormData ke `*-add-ajax/`). Tanggal selesai Experience dikirim sebagai `YYYY-MM-DDT00:00:00`, atau `null` jika dikosongkan.

## 4. Migrasi Permission untuk Editor

Migrasi `0004_create_editor_group` mencari permission `change_skill` dan `change_experience` saat database baru dibuat, padahal Django baru membuat baris Permission setelah semua migrasi selesai (sinyal `post_migrate`). Akibatnya Group Editor ada tetapi tanpa izin apa pun, dan Editor ditolak (403) saat mengedit pada database baru, seperti database pengujian dan kemungkinan database produksi. Migrasi `0005_ensure_editor_permissions` memperbaikinya: membuat Permission aplikasi `main` terlebih dulu, lalu menambahkannya ke Group Editor dengan `add()` (izin tambahan yang diberikan lewat admin tidak terhapus). `0006_merge_...` dibuat untuk menyatukan cabang migrasi setelah sempat terjadi konflik antara `0004` dan `0005`.

## 5. Fitur Tambahan: Statistik di Halaman Utama

Halaman utama mendapat bagian "Statistik Portofolio" di bawah profil. Datanya dihitung di server oleh `get_portfolio_stats()` saat halaman dibuka, tanpa JavaScript tambahan.

* Empat kartu angka: jumlah Skill, jumlah Experience, Experience yang sedang berlangsung, dan total star.
* Skill dan Experience terpopuler beserta jumlah star-nya. Jika jumlah star seri, dipilih judul pertama menurut abjad. Judulnya menjadi link ke halaman daftar dengan pencarian judul yang sudah terisi.
* Statistik terlihat oleh pengunjung tanpa login. Isinya hanya angka dan judul item, tanpa username, dan judul di-escape oleh template Django.
* Style memakai variabel warna tema yang sudah ada sehingga ikut menyesuaikan di dark mode.

## 6. Pengujian Otomatis

Dua file test baru, dijalankan dengan `python manage.py test main.tests_api main.tests_stats`.

* `tests_api.py` : satu set test yang dijalankan untuk `Skill` dan `Experience` sekaligus. Mencakup baca publik, pencarian dan filter kategori, jumlah query yang konstan, penolakan tulis untuk pengunjung dan pengguna biasa, Editor yang boleh PUT/PATCH tetapi ditolak saat create dan delete, alur empat peran, GET/OPTIONS yang tidak mengubah data, validasi dan pembersihan HTML, field read-only, star (toggle, filter `starred`, username tidak bocor), serta CSRF pada autentikasi sesi.
* `tests_stats.py` : database kosong, hitungan dan item terpopuler, pemutus seri, akses tanpa login tanpa kebocoran username, dan escaping judul.

## 7. Perbaikan Bug

* Tombol Edit rusak karena `.button-edit { width: 14%; margin-top: 0.5rem; }`. Diganti `width: auto; margin-top: 0`.
* Nama pemilik di header terlalu dekat dengan menu dan terpecah menjadi tiga baris. Header dan navigasi diberi `flex-wrap` dan `gap`, brand diberi `white-space: nowrap`.
* Tombol star terlalu dekat dengan teks status (Ongoing/Completed). Diberi jarak dan `align-self: flex-start`.
* Pada dark mode, judul dan label di dalam modal tampil hitam di atas latar gelap. Penyebabnya elemen `[popover]` memakai warna bawaan browser (`CanvasText`) dan tidak mewarisi `--ink`. Diperbaiki dengan `color: var(--ink)` pada keempat modal, ditambah `color-scheme` per tema agar kontrol bawaan browser (pemilih tanggal, dropdown, scrollbar) ikut gelap.
* Grup Editor tanpa izin pada database baru, diperbaiki lewat migrasi `0005` (lihat bagian 4).
* `show_experience` ternyata didefinisikan dua kali di `views.py`. Duplikatnya dihapus.
* Fungsi `showToast` lokal yang hanya mencetak ke console dan `escapeHtml` yang tertulis dua kali dihapus dari script halaman, sehingga toast dari `toast.js` yang dipakai.

### Tugas 6

1. Representational State Transfer (REST) adalah architectural style web yang memungkinkan aplikasi software berbeda untuk berkomunikasi melalui internet. REST memiliki prinsip-prinsip berupa antarmuka yang seragam, pemisahan antara client dan server, server tidak menyimpan state session (statelessness), cacheability, dan sistem yang berlapis.
JSON saja belum cukup untuk membuat sebuah API RESTful karena resourcenya masih berupa kata kerja di URL padahal seharusnya kata benda, method HTTPnya belum tentu menggunakan PUT PATCH DELETE, dan status code nya belum tentu bermakna semua. Ketiga tersebut diperlukan agar suatu API disebut sebagai RESTful.
PUT mengirimkan representasi lengkap dari suatu resource, sedangkan PATCH hanya mengirimkan field yang berubah (`partial=True`). PUT biasanya digunakan untuk form edit yang mengirim semua field atau sinkronisasi yang menimpa seluruh data, sedangkan PATCH biasanya digunakan untuk mengganti satu elemen saja seperti judul.

2. Serializer berguna untuk melakukan serialisasi, yaitu mengubah model atau queryset menjadi tipe Python sederhana dan merendernya menjadi JSON. Serializer juga memungkinkan dilakukannya deserialisasi, validasi data dan whitelist field.
Serializer unggul dibanding dictionary manual dengan JsonResponse karena menyediakan hanya satu sumber kebenaran, menghindari bug manual, memungkinkan penggunaan ulang validasi, menetapkan query agar tetap efisien, memudahkan pengujian, dan memiliki fleksibilitas lebih tinggi.

3. Autentikasi terkait dengan siapa yang menggunakan, sedangkan otorisasi terkait apa yang pengguna tertentu boleh lakukan (permissions-nya). Untuk autentikasi, Django menjalankan `authentication_classes` dan mengisi `request.user`. Sedangkan otorisasi dilakukan dengan menjalankan `permission_classes` setelah autentikasi. Di proyek ini, `isAuthenticated` untuk star, `IsPortfolioOwnerOrEditorOrReadOnly(Model)` untuk update dan delete menggunakan `has_perm("main.change_skill")`, dan lainnya.
Pemeriksaan hak akses harus dilakukan di server karena template hanya memberikan kenyamanan tanpa menyediakan keamanan, endpoint tetap ada meskipun tombolnya tidak ada (tetap bisa diakses), dan izin pengguna dapat dicabut setelah halaman dimuat. Sebaiknya yang dilakukan adalah menghilangkan tombol dan menyediakan keamanan pada server.

4. Token CSRF tetap diperlukan meskipun ada `SessionAuthentication` karena browser menempelkan cookie `sessionid` secara otomatis ke setiap request ke domain kita, termasuk request yang ditimbulkan dari halaman situs lain. Dengan itu, penyerang dapat membuat halaman di web lain yang mengirim POST atau DELETE secara tersembunyi ke API kita, dan browser juga akan mengirim session-nya. Server akan melihatnya sebagai request dari pengguna sah yang login sehingga request tersebut akan berhasil menyusup ke situs kita jika tidak ditangani dengan token CSRF atau keamanan lainnya.
Test yang menggunakan `force_authenticate` tidak cukup untuk membuktikan perlindungan CSRF karena `force_authenticate(user)` melewati proses autentikasi dan test client Django mematikan CSRF secara default sehingga test tersebut akan tetap lolos meskipun perlindungan CSRF tidak berfungsi. Untuk membuktikan aktifnya perlindungan CSRF, test harus menggunakan `APIClient(enforce_csrf_checks=True)` dan `client.login(...)`, POST tanpa token harus ditolak dengan kode 403, dan POST dengan token yang diambil dari halaman yang merender harus berhasil dengan kode 201.

AI Disclosure:
Menggunakan Claude Sonnet 5.5 Medium untuk membantu memahami materi terkait keamanan, REST dan RESTful APIs, serializer, dan lainnya. AI tersebut juga digunakan untuk membantu menerapkan fitur tambahan dan menyesuaikan kode tutorial dengan kode saya terkait serializer, permissions, API view, dan testing serta integrasi yang saya sesuaikan dan debug setelahnya, terutama saat ada yang menjadi rusak seperti elemen UI/UX (seperti teks form) yang menjadi berantakan pada kondisi tertentu seperti menghidupkan dark mode. 

Link Log Chat AI: https://claude.ai/share/b1a5464d-e43e-44ed-b65b-9dada64af40d