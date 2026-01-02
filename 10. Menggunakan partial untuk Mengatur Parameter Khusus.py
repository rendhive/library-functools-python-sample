import functools

def create_greeting(prefix, name):
    return f"{prefix}, {name}!"

greeting = functools.partial(create_greeting, "Hello")
print(greeting("Alice"))
# Fungsi: Membuat varian fungsi dengan nilai argumen tetap.
# Kondisi: Ketika Anda ingin membuat fungsi yang lebih spesifik dan mudah dipanggil.
