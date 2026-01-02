# Flask URL Shortener & QR Code Generator

Aplikasi web sederhana untuk memendekkan link panjang (URL Shortener) sekaligus membuat **QR Code** secara otomatis. Dibangun menggunakan Python (Flask) dengan tampilan antarmuka (UI) yang responsif dan modern.

Project ini menggunakan sistem database berbasis **JSON**, sehingga sangat ringan, mudah dipindahkan (portable), dan tidak memerlukan instalasi database server (MySQL/PostgreSQL).

## Fitur Utama
* **Custom Short Link:** User bisa menentukan sendiri kode unik link (contoh: `domain.com/diskon-januari`).
* **Auto QR Code:** Otomatis generate QR Code saat link berhasil dibuat.
* **No-Storage Image:** QR Code diproses di memori (RAM) dan dikirim via Base64, tidak memenuhi harddisk server.
* **Responsive UI:** Tampilan rapi di Laptop maupun HP.
* **JSON Database:** Data tersimpan di file `urls.json`, mudah dibaca dan diedit manual jika perlu.

## Teknologi yang Digunakan
* **Language:** Python 3.10
* **Framework:** Flask
* **Libraries:** qrcode, bytesio, pathlib, base64
* **Frontend:** HTML5, CSS3
* **Database:** JSON

---

## 📂 Struktur Folder
Pastikan struktur file Anda seperti ini agar aplikasi berjalan lancar:

```text
/project_folder
│
├── app.py              # File utama (Flask App)
├── database.py         # Logika penyimpanan data (CRUD JSON)
├── qr_generator.py     # Logika pembuatan QR Code (Base64)
├── urls.json           # File database (terbuat otomatis)
└── templates/          # FOLDER WAJIB untuk HTML
    └── index.html      # Tampilan antarmuka web