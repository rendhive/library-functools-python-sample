import functools

def decorator(func):
    @functools.wraps(func)  # Menjaga nama dan docstring asli
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def example_function():
    """This is an example function."""
    return "Hello"

print("Nama fungsi:", example_function.__name__)
print("Docstring:", example_function.__doc__)
# Fungsi: Menggunakan wraps untuk menjaga informasi fungsi asli.
# Kondisi: Ketika Anda mengimplementasikan dekorator di sekitar fungsi lainnya.
