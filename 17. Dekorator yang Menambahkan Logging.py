import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Memanggil fungsi: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def sample_function():
    return "Fungsi ini berfungsi."

print(sample_function())
# Fungsi: Menambahkan logging ke fungsi untuk memantau pelaksanaan.
# Kondisi: Ketika Anda ingin mencatat informasi eksekusi selama pemanggilan fungsi.
