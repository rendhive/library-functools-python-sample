import functools

def coroutine(func):
    """Decorator to automatically prime a coroutine."""
    @functools.wraps(func)
    def start(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Prime the generator
        return gen
    return start

@coroutine
def greet():
    while True:
        name = (yield)
        print(f"Hello, {name}!")

g = greet()
g.send("Alice")
g.send("Bob")
# Fungsi: Menggunakan dekorator untuk mengatur generator secara otomatis.
# Kondisi: Ketika Anda perlu memodifikasi perilaku fungsi generator.
