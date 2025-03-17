import pandas as pd
import numpy as np
import os
import sys

class BookManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.exists(file_path):
            self.book = pd.read_excel(file_path)
        else:
            self.book = pd.DataFrame(columns=['Judul', 'Penulis', 'Penerbit', 'Tahun','Kategori', 'ISBN', 'Halaman', 'Deskripsi' ])

    def save(self):
        self.book.to_excel(self.file_path, index=False)
        return True
    
    def getBook(self):
        return self.book
    
    def getBookByIsbn(self, isbn):
        if isbn not in self.book['ISBN'].values:
            return None
        
        return self.book[self.book['ISBN'] == isbn].iloc[0]
    
    def getBookByIndex(self, index):
        if index < 0 or index >= len(self.book):
            return None
        
        return self.book.iloc[index]
    
    def searchBooks(self, query, field="Judul"):
        query = query.lower()  # Pastikan query dalam huruf kecil

        if field in self.book.columns:
            # Gunakan regex untuk mencari substring tanpa case-sensitive
            filtered_book = self.book[self.book[field].astype(str).str.contains(query, case=False, na=False)]
        elif field == "all":
            # Pencarian di semua kolom
            mask = self.book.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)
            filtered_book = self.book[mask]
        else:
            return []  # Jika field tidak valid, kembalikan list kosong

        return filtered_book#.to_dict(orient="records")  # Konversi hasil ke list of dictionary
        
    def getBooksByField(self, field, value):
        if field not in self.book.columns:
            return pd.DataFrame()
        
        if field in ['Judul', 'Penulis', 'Penerbit', 'ISBN', 'Kategori', 'Deskripsi']:
            hasil = self.book[self.book[field].str.contains(str(value), case=False, na=False)]
        else:
            hasil = self.book[self.book[field] == value]
        
        return hasil
    
    def addBook(self, judul, pengarang, penerbit, tahun, isbn):
        if isbn in self.book['ISBN'].values:
            return False
        
        if len(self.book) > 0:
            nomor = self.book['No'].max() + 1
        else:
            nomor = 1
        
        buku_baru = {
            'No': nomor,
            'Judul': judul,
            'Pengarang': pengarang,
            'Penerbit': penerbit,
            'Tahun': tahun,
            'ISBN': isbn
        }
        
        self.book = pd.concat([self.book, pd.DataFrame([buku_baru])], ignore_index=True)
        return True
    
    def updateBook(self, isbn, **kwargs):
        if isbn not in self.book['ISBN'].values:
            return False
        
        for field, value in kwargs.items():
            if field in ['Judul', 'Pengarang', 'Penerbit', 'Tahun']:
                self.book.loc[self.book['ISBN'] == isbn, field] = value
        
        return True
    
    def deleteBook(self, isbn):
        if isbn not in self.book['ISBN'].values:
            return False
        
        self.book = self.book[self.book['ISBN'] != isbn]
        self.book = self.book.reset_index(drop=True)
        self.book['No'] = self.book.index + 1
        
        return True
    
    def getColumnValues(self, column):
        if column not in self.book.columns:
            return []
        
        return self.book[column].unique().tolist()
    
    def getBookCount(self):
        return len(self.book)
    
    def daftarPenulis(self):
        return self.book.drop_duplicates(subset='Penulis')['Penulis'].tolist()
    
    def daftarKategori(self):
        return self.book['Kategori'].unique().tolist()
    
    def daftarPenerbit(self):
        return self.book['Penerbit'].unique().tolist()
    
