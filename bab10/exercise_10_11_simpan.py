import json
from pathlib import Path

number = input("Berapa angka favorit Anda? ")
path = Path('Latihan-Prokom-B-Muhammad-Rizki/text_bab10/favorite_number.json')

# Menggunakan json.dumps() untuk mengubah angka menjadi string JSON lalu disimpan
contents = json.dumps(number)
path.write_text(contents)

print("Angka favorit Anda telah disimpan!")