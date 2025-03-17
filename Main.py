from BookManager import BookManager

book = BookManager("data_buku.xlsx")

# book.book.info()

# print(book.book)

# print(book.book.sort_values(by="Judul", ascending=False))
print(book.daftarKategori())