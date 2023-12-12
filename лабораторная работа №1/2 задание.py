# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
disk = 1.44 * 1024 * 1024
bytes_per_symbol = 4

total_symbols = pages * lines * symbols
total_bytes = total_symbols * bytes_per_symbol

books_on_disk = disk// total_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
