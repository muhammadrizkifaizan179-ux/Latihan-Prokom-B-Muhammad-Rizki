import json
from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/text_bab10/favorite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("Berapa angka favorit Anda? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Kami akan mengingat angka favorit Anda!")