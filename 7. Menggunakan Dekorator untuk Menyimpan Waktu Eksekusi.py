import functools
import time

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def calculate_sum(n):
    return sum(range(n))

calculate_sum(100000)
# Fungsi: Mengukur dan melaporkan waktu eksekusi fungsi.
# Kondisi: Ketika Anda perlu memantau kinerja atau waktu eksekusi fungsi.
