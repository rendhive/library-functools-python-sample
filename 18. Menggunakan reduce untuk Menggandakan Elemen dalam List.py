import functools

data = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, data)

print("Produk dari data:", product)
# Fungsi: Menggunakan reduce untuk menghitung produk dari seluruh elemen.
# Kondisi: Ketika Anda perlu mengalikan semua elemen dalam koleksi.
