import struct

class Buku:
    def __init__(self, judul, pengarang, nomer_isbn, penerbit, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.nomer_isbn = nomer_isbn
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit

def pack_buku(buku):
    return struct.pack('100s100s20s50sI', 
                       buku.judul.encode('utf-8'), 
                       buku.pengarang.encode('utf-8'), 
                       buku.nomer_isbn.encode('utf-8'), 
                       buku.penerbit.encode('utf-8'), 
                       buku.tahun_terbit)

def unpack_buku(data):
    unpacked_data = struct.unpack('100s100s20s50sI', data)
    judul = unpacked_data[0].decode('utf-8').rstrip('\x00')
    pengarang = unpacked_data[1].decode('utf-8').rstrip('\x00')
    nomer_isbn = unpacked_data[2].decode('utf-8').rstrip('\x00')
    penerbit = unpacked_data[3].decode('utf-8').rstrip('\x00')
    tahun_terbit = unpacked_data[4]
    
    return Buku(judul, pengarang, nomer_isbn, penerbit, tahun_terbit)

def simpan_buku(data_buku, nama_file):
    with open(nama_file, 'wb') as file:
        for buku in data_buku:
            packed_data = pack_buku(buku)
            file.write(packed_data)

def baca_buku(nama_file):
    try:
        with open(nama_file, 'rb') as file:
            while True:
                packed_data = file.read(struct.calcsize('100s100s20s50sI'))
                if not packed_data:
                    break
                buku = unpack_buku(packed_data)
                print("Judul:", buku.judul)
                print("Pengarang:", buku.pengarang)
                print("Nomor ISBN:", buku.nomer_isbn)
                print("Penerbit:", buku.penerbit)
                print("Tahun Terbit:", buku.tahun_terbit)
                print("\n")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def tambah_buku(nama_file, buku_baru):
    try:
        with open(nama_file, 'ab') as file:
            packed_data = pack_buku(buku_baru)
            file.write(packed_data)
        print("Buku baru berhasil ditambahkan.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def ubah_buku(nama_file, nomer_isbn, data_baru):
    with open(nama_file, 'rb+') as file:
        while True:
            packed_data = file.read(struct.calcsize('100s100s20s50sI'))
            if not packed_data:
                break
            buku = unpack_buku(packed_data)
            if buku.nomer_isbn == nomer_isbn:
                buku.judul = data_baru['judul']
                buku.pengarang = data_baru['pengarang']
                buku.nomer_isbn = data_baru['nomer_isbn']
                buku.penerbit = data_baru['penerbit']
                buku.tahun_terbit = data_baru['tahun_terbit']
                file.seek(-struct.calcsize('100s100s20s50sI'), 1)
                file.write(pack_buku(buku))
                print("Data buku berhasil diubah.")
                return
        print("Buku dengan Nomor ISBN tersebut tidak ditemukan.")

def hapus_buku(nama_file, nomer_isbn):
    with open(nama_file, 'rb+') as file:
        data_buku = []
        while True:
            posisi_sekarang = file.tell()
            packed_data = file.read(struct.calcsize('100s100s20s50sI'))
            if not packed_data:
                break
            buku = unpack_buku(packed_data)
            if buku.nomer_isbn != nomer_isbn:
                data_buku.append(buku)

        file.seek(0)
        for buku in data_buku:
            packed_data = pack_buku(buku)
            file.write(packed_data)

        file.truncate()
        print("Data buku berhasil dihapus.")

# Contoh penggunaan
if __name__ == "__main__":
    nama_file = "data_buku.bin"

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Lihat Data Buku")
        print("3. Ubah Data Buku")
        print("4. Hapus Data Buku")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            judul = input("Judul: ")
            pengarang = input("Pengarang: ")
            nomer_isbn = input("Nomor ISBN: ")
            penerbit = input("Penerbit: ")
            tahun_terbit = int(input("Tahun Terbit: "))
            buku_baru = Buku(judul, pengarang, nomer_isbn, penerbit, tahun_terbit)
            tambah_buku(nama_file, buku_baru)
        elif pilihan == '2':
            baca_buku(nama_file)
        elif pilihan == '3':
            nomer_isbn = input("Masukkan Nomor ISBN buku yang ingin diubah: ")
            judul = input("Judul baru: ")
            pengarang = input("Pengarang baru: ")
            penerbit = input("Penerbit baru: ")
            tahun_terbit = int(input("Tahun Terbit baru: "))
            data_baru = {'judul': judul, 'pengarang': pengarang, 'nomer_isbn': nomer_isbn,
                         'penerbit': penerbit, 'tahun_terbit': tahun_terbit}
            ubah_buku(nama_file, nomer_isbn, data_baru)
        elif pilihan == '4':
            nomer_isbn = input("Masukkan Nomor ISBN buku yang ingin dihapus: ")
            hapus_buku(nama_file, nomer_isbn)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
