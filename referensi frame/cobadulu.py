# Import library yang diperlukan
import pandas as pd

# 1. Membaca file CSV
def baca_data_buku(nama_file):
    try:
        df = pd.read_csv(nama_file)
        print(f"Berhasil membaca file {nama_file}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

# 2. Menampilkan informasi awal data
def info_data(df):
    print("\nInformasi Data:")
    print(f"Jumlah buku: {len(df)}")
    print("\nLima data pertama:")
    print(df.head())
    print("\nInformasi kolom:")
    print(df.info())
    print("\nStatistik deskriptif:")
    print(df.describe(include='all'))

# 3. Mencari buku berdasarkan judul
def cari_buku(df, judul):
    hasil = df[df['judul'].str.contains(judul, case=False)]
    return hasil

# 4. Menyortir buku (misalnya berdasarkan tahun terbit)
def sortir_buku(df, kolom, ascending=True):
    return df.sort_values(by=kolom, ascending=ascending)

# 5. Menambah buku baru
def tambah_buku(df, data_buku_baru):
    return pd.concat([df, pd.DataFrame([data_buku_baru])], ignore_index=True)

# 6. Memperbarui informasi buku
def update_buku(df, index, kolom, nilai_baru):
    df.loc[index, kolom] = nilai_baru
    return df

# 7. Menyimpan perubahan ke file CSV
def simpan_ke_csv(df, nama_file):
    df.to_csv(nama_file, index=False)
    print(f"Data berhasil disimpan ke {nama_file}")

# 8. Menghapus buku
def hapus_buku(df, index):
    return df.drop(index)

# 9. Mengelompokkan buku berdasarkan kategori
def kelompokkan_buku(df, kolom):
    return df.groupby(kolom).size().reset_index(name='jumlah')

# Contoh penggunaan
if __name__ == "__main__":
    # Ganti dengan nama file CSV Anda
    nama_file = "Cobaaa\\Books.csv"
    
    # Membaca data
    data_buku = baca_data_buku(nama_file)
    
    if data_buku is not None:
        # Menampilkan informasi data
        info_data(data_buku)
        
        # Mencari buku dengan judul tertentu
        print("\nHasil pencarian buku 'Python':")
        hasil_cari = cari_buku(data_buku, "Python")
        print(hasil_cari)
        
        # Menyortir buku berdasarkan tahun terbit
        print("\nBuku diurutkan berdasarkan tahun terbit:")
        buku_urut = sortir_buku(data_buku, 'tahun_terbit')
        print(buku_urut.head())
        
        # Menambah buku baru
        buku_baru = {
            'judul': 'Python Data Science Handbook',
            'penulis': 'Jake VanderPlas',
            'penerbit': 'O\'Reilly Media',
            'tahun_terbit': 2016,
            'genre': 'Programming',
            'harga': 150000
        }
        data_buku = tambah_buku(data_buku, buku_baru)
        print("\nBuku baru telah ditambahkan")
        
        # Menyimpan perubahan
        simpan_ke_csv(data_buku, "data_buku_update.csv")