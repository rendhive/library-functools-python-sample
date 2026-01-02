import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()
# Fungsi: Menggunakan dekorator untuk mendekorasi fungsi dengan parameter.
# Kondisi: Ketika Anda ingin menerapkan perilaku yang sama beberapa kali.
