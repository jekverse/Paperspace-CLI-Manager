# Paperspace Gradient CLI Manager

Solusi untuk kalian yang tidak suka dengan UI interface Paperspace Gradient yang lambat dan sering bermasalah! Repo ini menyediakan sebuah manajer berbasis CLI yang cepat dan efisien tanpa perlu bergantung pada antarmuka web.

Dengan menggunakan repo ini, kalian bisa melakukan pengaturan pada notebook di Paperspace Gradient langsung melalui terminal, tanpa perlu menunggu UI web yang lambat dan sering mengalami bug.

## Fitur

Berikut beberapa fungsi utama dari `Paperspace Gradient CLI Manager`:

1. **Membuat notebook baru**: Buat notebook langsung dari terminal tanpa melalui antarmuka web.
2. **Menjalankan, menghentikan, dan menghapus notebook**: Kontrol penuh atas notebook yang kamu miliki, langsung dari command line.
3. **Melihat ketersediaan machine**: Cek ketersediaan GPU atau machine lainnya secara cepat dan real-time.
4. **Melihat detail notebook**: Dapatkan informasi lengkap mengenai notebook yang sedang kamu kelola.

## Fitur Menarik

Selain fungsi dasar di atas, repo ini juga memiliki fitur unggulan yang tidak tersedia di Paperspace Gradient Web:

1. **Mengatasi batasan sesi notebook 6 jam**: Secara otomatis memantau notebook, dan menyalakan kembali notebook ketika mati karena melebihi batas waktu 6 jam.
2. **Otomatis mengecek ketersediaan machine GPU**: Jika machine GPU yang kamu inginkan tidak tersedia, skrip ini akan terus mengecek secara otomatis setiap 30 detik hingga GPU tersedia, tanpa perlu melakukan pengecekan manual.

Repo ini terus dikembangkan dengan fitur-fitur tambahan yang akan datang!