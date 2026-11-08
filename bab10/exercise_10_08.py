from pathlib import Path

filenames = ['Latihan-Prokom-B-Muhammad-Rizki/text_bab10/cats.txt', 'Latihan-Prokom-B-Muhammad-Rizki/text_bab10/dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        print(f"Isi {filename}:\n{contents}")