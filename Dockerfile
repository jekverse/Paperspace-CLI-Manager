# Menggunakan base image Python 3.7 slim
FROM python:3.7-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Mengatur direktori kerja di dalam container
WORKDIR /app

# Menyalin requirements.txt jika Anda memilikinya (opsional)
COPY requirements.txt .

# Menginstal dependensi (opsional)
RUN pip install -r requirements.txt

# Menyalin semua file dari direktori lokal ke dalam container
COPY . .

# Menjalankan main.py
CMD ["python", "main.py"]
