import functools

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Faktorial 5:", factorial(5))
# Fungsi: Mengoptimalkan fungsi faktorial untuk efisiensi.
# Kondisi: Ketika Anda perlu menghitung nilai yang sering dipanggil kembali.
