import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(10):", fibonacci(10))
# Fungsi: Mengoptimalkan fungsi dengan menyimpan cache hasil komputasi.
# Kondisi: Ketika Anda ingin menghindari penghitungan berulang untuk fungsi berbiaya tinggi.
