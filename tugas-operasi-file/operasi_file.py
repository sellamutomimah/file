def membaca(nama_file):
    with open(nama_file, "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis(nama_file):
    
    membaca("file.txt")

    nama_bunga = input("Nama bunga: ")
    text = "\n {}".format(nama_bunga)


    with open(nama_file, "a") as file_bunga:
        file_bunga.write(text)

menulis("file.txt")