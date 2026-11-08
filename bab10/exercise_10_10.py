from pathlib import Path

filenames = ['Latihan-Prokom-B-Muhammad-Rizki/text_bab10/alice_in_wonderland.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        count_the = contents.lower().count('the')
        count_the_space = contents.lower().count('the ')
        print(f"{filename}: 'the' muncul {count_the} kali, 'the ' muncul {count_the_space} kali.")