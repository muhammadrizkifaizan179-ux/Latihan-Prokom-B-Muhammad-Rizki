import json
from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/text_bab10/favorite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
else:
    print("File angka favorit belum ditemukan.")