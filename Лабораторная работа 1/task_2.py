# TODO Найдите количество книг, которое можно разместить на дискете

floppy_drive_size_mb = 1.44
pages_in_each_book = 100
lines_on_the_page = 50
symbols_in_the_line = 25
size_of_symbol = 4
kb = 1024  # Размер килобайта в байтах
mb = 1024
floppy_drive_size_bytes = floppy_drive_size_mb * mb * kb
books_num = int(floppy_drive_size_bytes / (pages_in_each_book * lines_on_the_page *
                                           symbols_in_the_line * size_of_symbol))

print("Количество книг, помещающихся на дискету:", books_num)
