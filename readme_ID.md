# Paperspace CLI Manager
![Screenshot Project](./img/Image1.jpg)

[English](readme.md) | [Bahasa Indonesia](readme_ID.md)

**Paperspace CLI Manager** adalah solusi ideal bagi pengguna yang merasa terganggu dengan antarmuka UI Paperspace Gradient yang lambat dan sering penuh bug. Dengan manajer berbasis CLI ini, Anda dapat mengelola notebook di Paperspace Gradient secara cepat dan efisien melalui terminal, tanpa harus bergantung pada UI web.

Dengan repo ini, Anda dapat melakukan berbagai pengaturan dan manajemen notebook langsung dari command line, menghilangkan kebutuhan untuk menunggu antarmuka web yang sering kali lambat.

## Fitur

Berikut adalah fitur-fitur utama dari **Paperspace CLI Manager**:

1. **Membuat notebook baru**: Buat notebook langsung dari terminal tanpa melalui UI web.
2. **Menjalankan, menghentikan, dan menghapus notebook**: Kendalikan notebook Anda sepenuhnya dari command line.
3. **Melihat ketersediaan mesin**: Cek ketersediaan GPU atau mesin lain secara real-time dan cepat.
4. **Melihat detail notebook**: Dapatkan informasi mendetail mengenai notebook yang sedang Anda kelola.

## Fitur Unggulan

Selain fungsi dasar di atas, repo ini juga memiliki fitur unggulan yang tidak tersedia di antarmuka web Paperspace Gradient:

1. **Mengatasi batasan sesi notebook 6 jam**: Secara otomatis memantau notebook dan menyalakan kembali jika mati karena mencapai batas waktu 6 jam.
2. **Otomatis memeriksa ketersediaan GPU**: Jika GPU yang diinginkan tidak tersedia, skrip ini akan memeriksa ketersediaan setiap 30 detik hingga GPU tersedia, menghilangkan kebutuhan untuk pengecekan manual.

Repo ini akan terus dikembangkan dengan berbagai fitur tambahan di masa mendatang!

## Instalasi

### Menggunakan Virtual Environment

Untuk menghindari konflik dependensi, sangat disarankan untuk menggunakan **virtual environment (venv)** pada Python. Pastikan Anda menggunakan **Python versi 3.7** sebelum melanjutkan.

1. **Pastikan Python 3.7 sudah terinstal**:
   Jika belum, silakan unduh dan instal Python versi 3.7 dari [python.org](https://www.python.org/downloads/release/python-370/).

2. **Buat virtual environment**:
   Buat virtual environment dengan Python 3.7 untuk mencegah konflik dependensi:
   ```bash
   python3.7 -m venv venv
   ```

3. **Aktifkan virtual environment**:
   - Di macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Di Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Instal paket yang diperlukan**:
   Setelah virtual environment aktif, instal paket yang dibutuhkan dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup Token & Project_ID Paperspace**:
   Setelah semua paket terinstal, jalankan `Masukan Token & Project_ID Paperspace` dengan perintah:
   ```bash
   python main.py
   ```
6. **Jalankan Paperspace CLI Manager**:
   Jalankan `Paperspace Gradient CLI Manager` dengan perintah:
   ```bash
   python main.py
   ```

### Menggunakan Docker

Untuk penggunaan yang lebih mudah, Anda juga dapat menjalankan **Paperspace CLI Manager** menggunakan Docker. Berikut adalah langkah-langkahnya:

1. **Pastikan Docker sudah terinstal di komputer Anda**.
2. **Jalankan setup.py**:
   ```bash
   python3 setup.py
   ```
3. **Build Docker image**:
   ```bash
   docker build -t paperspace-cli-manager .
   ```
   Tunggu hingga proses build selesai.
4. **Jalankan dengan Docker**:
   ```bash
   docker run -it --rm paperspace-cli-manager
   ```

Setelah langkah-langkah di atas selesai, Anda siap menggunakan **Paperspace Gradient CLI Manager** di lingkungan yang telah Anda atur.

## Kontributor

Repo ini dibuat dengan dedikasi oleh saya dan sahabat baik saya, **ChatGPT**. Kami berkolaborasi untuk memberikan solusi cepat dan efisien bagi pengguna Paperspace Gradient yang lebih menyukai penggunaan command line.
