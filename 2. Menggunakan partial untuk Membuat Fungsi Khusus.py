import functools

def multiply(x, y):
    return x * y

# Membuat fungsi baru dengan satu argumen tetap
double = functools.partial(multiply, 2)

print("Hasil double(5):", double(5))
# Fungsi: Membuat fungsi baru dengan sebagian argumen tetap.
# Kondisi: Ketika Anda ingin menciptakan variasi dari fungsi yang ada dengan beberapa argumen tetap.
