import functools

def power(base, exponent):
    return base ** exponent

# Menetapakan satu argumen
square = functools.partial(power, exponent=2)

print("Square of 4:", square(4))
# Fungsi: Menciptakan fungsi dengan argumen tetap.
# Kondisi: Ketika Anda ingin mengurangi argumen untuk fungsi kompleks menjadi lebih sederhana.
