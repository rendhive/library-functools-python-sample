import functools

data = [1, 2, 3, 4, 5]
total = functools.reduce(lambda x, y: x + y, data)

print("Total dari data:", total)
# Fungsi: Menggunakan reduce untuk mengagregasi elemen menjadi satu nilai.
# Kondisi: Ketika Anda perlu menjalankan fungsi agregasi pada koleksi.
