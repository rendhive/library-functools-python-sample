import functools

def sort_list(key, reverse, data):
    return sorted(data, key=key, reverse=reverse)

# Membuat fungsi sortir untuk urutan asc
ascending_sort = functools.partial(sort_list, key=lambda x: x)

data = [3, 1, 4, 1, 5]
sorted_data = ascending_sort(reverse=False, data=data)

print("Data setelah diurutkan:", sorted_data)
# Fungsi: Mengurangi argumen untuk fungsi sortir menjadi lebih mudah dipanggil.
# Kondisi: Ketika Anda sering melakukan operasi sortir pada koleksi berbeda.
