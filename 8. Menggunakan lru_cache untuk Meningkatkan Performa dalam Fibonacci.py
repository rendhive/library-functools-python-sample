import functools

@functools.lru_cache(maxsize=100)
def efficient_fibonacci(n):
    if n < 2:
        return n
    return efficient_fibonacci(n - 1) + efficient_fibonacci(n - 2)

print("Efficient Fibonacci(20):", efficient_fibonacci(20))
# Fungsi: Menggunakan caching untuk meningkatkan efisiensi fungsi rekursif.
# Kondisi: Ketika Anda perlu frekuensi panggilan fungsi yang tinggi dengan parameter yang sama.
