
import json
from pathlib import Path

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("Siapa nama Anda? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('Latihan-Prokom-B-Muhammad-Rizki/text_bab10/username.json')
    username = get_stored_username(path)
    
    if username:
        correct = input(f"Apakah nama Anda {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
            return
            
    username = get_new_username(path)
    print(f"Kami akan mengingat Anda saat kembali, {username}!")

greet_user()