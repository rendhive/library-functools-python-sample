import functools

@functools.lru_cache(maxsize=128)
def calculate_power(base, exponent):
    return base ** exponent

print("2^5:", calculate_power(2, 5))
print("3^3:", calculate_power(3, 3))
# Fungsi: Menggunakan caching untuk menghindari penghitungan sama.
# Kondisi: Ketika hasil fungsi memerlukan perhitungan berat dan sering dipanggil dengan argumen yang sama.
