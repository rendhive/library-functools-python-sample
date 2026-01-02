import functools

def decorator_function(original_function):
    @functools.wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    return "Display function executed."

print(display())
# Fungsi: Menggunakan dekorator untuk menambahkan fungsionalitas tanpa kehilangan informasi fungsi asli.
# Kondisi: Ketika Anda ingin mendekorasi fungsi dan menjaga metadata asli.
