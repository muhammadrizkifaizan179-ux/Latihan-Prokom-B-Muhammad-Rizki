from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/bab10/name_guest.txt')

name = input("Masukkan nama Anda: ")

# Menulis teks ke file menggunakan write_text()
path.write_text(name)

print(f"Nama '{name}' telah berhasil disimpan ke {path.name}.")