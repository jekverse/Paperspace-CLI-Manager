# Paperspace Gradient CLI Manager

Paperspace Gradient CLI Manager adalah solusi bagi pengguna yang merasa terganggu dengan antarmuka UI Paperspace Gradient yang sering lambat dan penuh bug. Dengan manajer berbasis CLI ini, Anda dapat mengelola notebook di Paperspace Gradient secara cepat dan efisien melalui terminal, tanpa harus bergantung pada UI web.

Dengan repo ini, Anda bisa melakukan berbagai pengaturan dan manajemen notebook langsung dari command line, menghilangkan kebutuhan untuk menunggu antarmuka web yang sering kali lambat.

## Fitur

Berikut adalah fitur-fitur utama dari `Paperspace Gradient CLI Manager`:

1. **Membuat notebook baru**: Membuat notebook langsung dari terminal tanpa melalui UI web.
2. **Menjalankan, menghentikan, dan menghapus notebook**: Kendalikan notebook Anda sepenuhnya dari command line.
3. **Melihat ketersediaan machine**: Cek ketersediaan GPU atau mesin lain secara real-time dan cepat.
4. **Melihat detail notebook**: Dapatkan informasi mendetail mengenai notebook yang sedang Anda kelola.

## Fitur Unggulan

Selain fungsi dasar di atas, repo ini juga memiliki beberapa fitur unggulan yang tidak tersedia di antarmuka web Paperspace Gradient:

1. **Mengatasi batasan sesi notebook 6 jam**: Repo ini secara otomatis memantau notebook, dan akan menyalakan kembali notebook jika mati karena mencapai batas waktu 6 jam.
2. **Otomatis memeriksa ketersediaan GPU**: Jika GPU yang diinginkan tidak tersedia, skrip ini akan secara otomatis memeriksa ketersediaan setiap 30 detik hingga GPU tersedia, menghilangkan kebutuhan untuk pengecekan manual.

Repo ini akan terus dikembangkan dengan berbagai fitur tambahan di masa mendatang!

## Instalasi

Untuk menghindari konflik dependensi, sangat disarankan menggunakan **virtual environment (venv)** pada Python. Repo ini membutuhkan **Python versi 3.7**, jadi pastikan Anda telah menginstal versi Python yang sesuai sebelum melanjutkan.

Berikut adalah langkah-langkah instalasi:

1. **Pastikan Python 3.7 sudah terinstal**:
   Jika belum, silakan download dan instal Python versi 3.7 dari [python.org](https://www.python.org/downloads/release/python-370/).

2. **Buat virtual environment**:
   Buat virtual environment dengan Python 3.7 agar tidak terjadi konflik dependensi.
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
   Setelah virtual environment aktif, instal paket-paket yang dibutuhkan dengan perintah berikut:
   ```bash
   pip install gradient
   pip install pytz
   pip install python-dotenv
   ```

Setelah langkah-langkah di atas selesai, Anda siap menggunakan `Paperspace Gradient CLI Manager` di lingkungan virtual yang sudah diatur.