# 📚 Sistem Manajemen Data Buku (Python + Binary File)

Proyek ini adalah **aplikasi console sederhana** untuk mengelola data buku menggunakan **Python** dengan penyimpanan **file biner** (`.bin`).
Aplikasi ini memanfaatkan modul **`struct`** untuk melakukan proses **packing** dan **unpacking** data agar efisien dalam penyimpanan.

## ✨ Fitur Utama

* **Tambah Buku** – Menyimpan data buku baru ke dalam file biner.
* **Lihat Data Buku** – Menampilkan semua data buku yang tersimpan.
* **Ubah Data Buku** – Memperbarui informasi buku berdasarkan **Nomor ISBN**.
* **Hapus Buku** – Menghapus data buku tertentu.
* **Penyimpanan Efisien** – Menggunakan `struct` untuk format biner yang terstruktur.

## 🛠 Struktur Data

Setiap buku disimpan dengan format:

| Field        | Tipe Data | Panjang Maksimum |
| ------------ | --------- | ---------------- |
| Judul        | String    | 100 karakter     |
| Pengarang    | String    | 100 karakter     |
| Nomor ISBN   | String    | 20 karakter      |
| Penerbit     | String    | 50 karakter      |
| Tahun Terbit | Integer   | 4 byte           |

Format `struct`:

```
100s 100s 20s 50s I
```

## 📂 Contoh Penggunaan

```bash
Menu:
1. Tambah Buku
2. Lihat Data Buku
3. Ubah Data Buku
4. Hapus Data Buku
5. Keluar
```

Contoh penambahan buku:

```
Judul: Belajar Python
Pengarang: Edo Pramudya
Nomor ISBN: 1234567890
Penerbit: OpenAI Press
Tahun Terbit: 2025
Buku baru berhasil ditambahkan.
```
