import functools

@functools.lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Apakah 19 bilangan prima?", is_prime(19))
# Fungsi: Mengoptimalkan pemeriksaan bilangan prima dengan caching.
# Kondisi: Ketika Anda perlu melakukan pemeriksaan berulang pada bilangan.
