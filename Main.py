import pandas as pd
import numpy as np

buku = pd.read_excel('data_buku.xlsx')

# print(buku)
# print(buku['Judul'].values)
# print(buku['ISBN'].values)
# print(buku['Pengarang'][0])
# print(buku['Penerbit'][0])
# print(buku['Tahun'][0])


# print(buku[buku['ISBN'] == 2019].values)
# print("\n\n\n")
# print(buku[buku['Judul'].str.contains('Pan')].values)
buku = buku[buku['Judul'].str.contains('Pan')].values

print(buku)