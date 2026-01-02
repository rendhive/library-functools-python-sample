import functools

@functools.lru_cache(maxsize=None)
def square(n):
    return n * n

print("Square of 4:", square(4))
print("Square of 4 (cached):", square(4))
# Fungsi: Menggunakan caching untuk menghindari penghitungan ulang.
# Kondisi: Ketika Anda ingin mempercepat aplikasi dengan menyimpan hasil fungsi yang sering dipanggil.
