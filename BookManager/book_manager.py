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
            self.book = pd.DataFrame(columns=['No', 'Judul', 'Pengarang', 'Penerbit', 'Tahun', 'ISBN', 'Status'])
    
    def save(self):
        self.book.to_excel(self.file_path, index=False)
        return True
    
    def getBook(self):
        return self.book
    
    def get_book_by_isbn(self, isbn):
        if isbn not in self.book['ISBN'].values:
            return None
        
        return self.book[self.book['ISBN'] == isbn].iloc[0]
    
    def get_book_by_index(self, index):
        if index < 0 or index >= len(self.book):
            return None
        
        return self.book.iloc[index]
    
    def get_books_by_field(self, field, value):
        if field not in self.book.columns:
            return pd.DataFrame()
        
        if field in ['Judul', 'Pengarang', 'Penerbit', 'ISBN']:
            hasil = self.book[self.book[field].str.contains(str(value), case=False, na=False)]
        else:
            hasil = self.df[self.df[field] == value]
        
        return hasil
    
    def add_book(self, judul, pengarang, penerbit, tahun, isbn):
        if isbn in self.df['ISBN'].values:
            return False
        
        if len(self.df) > 0:
            nomor = self.df['No'].max() + 1
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
        
        self.df = pd.concat([self.df, pd.DataFrame([buku_baru])], ignore_index=True)
        return True
    
    def update_book(self, isbn, **kwargs):
        if isbn not in self.df['ISBN'].values:
            return False
        
        for field, value in kwargs.items():
            if field in ['Judul', 'Pengarang', 'Penerbit', 'Tahun']:
                self.df.loc[self.df['ISBN'] == isbn, field] = value
        
        return True
    
    def delete_book(self, isbn):
        if isbn not in self.df['ISBN'].values:
            return False
        
        self.df = self.df[self.df['ISBN'] != isbn]
        self.df = self.df.reset_index(drop=True)
        self.df['No'] = self.df.index + 1
        
        return True
    
    def get_column_values(self, column):
        if column not in self.df.columns:
            return []
        
        return self.df[column].unique().tolist()
    
    def get_book_count(self):
        return len(self.df)