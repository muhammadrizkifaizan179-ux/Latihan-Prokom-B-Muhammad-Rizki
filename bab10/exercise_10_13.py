import json
from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/text_bab10/user_info.json')

if path.exists():
    user = json.loads(path.read_text())
    print("Data yang kuingat tentangmu:")
    print(f"- Nama : {user['name']}")
    print(f"- Kota : {user['city']}")
    print(f"- Hobi : {user['hobby']}")
else:
    user = {
        'name': input("Siapa namamu? "),
        'city': input("Kamu tinggal di kota mana? "),
        'hobby': input("Apa hobimu? "),
    }
    path.write_text(json.dumps(user))
    print("Datamu sudah kusimpan.")