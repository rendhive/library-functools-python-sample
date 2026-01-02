import functools
import time

def debounce(wait):
    def decorator(fn):
        @functools.wraps(fn)
        def debounced(*args, **kwargs):
            time.sleep(wait)
            return fn(*args, **kwargs)
        return debounced
    return decorator

@debounce(2)
def print_message(message):
    print(message)

print_message("Ini akan muncul setelah 2 detik.")
# Fungsi: Menggunakan dekorator untuk menunda eksekusi fungsi.
# Kondisi: Ketika Anda ingin membatasi panggilan cepat ke fungsi, seperti pengendalian event.
