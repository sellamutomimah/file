#buka file
file_pantun = open ("pantun.txt", "r")

#baca isi file
pantun = file_pantun.read()

#cetak isi file
print (pantun)

#tutup file
file_pantun .close()