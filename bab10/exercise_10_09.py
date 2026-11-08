from pathlib import Path

filenames = ['Latihan-Prokom-B-Muhammad-Rizki/text_bab10/cats.txt', 'Latihan-Prokom-B-Muhammad-Rizki/text_bab10/dogs.txt']

for filename in filenames:
    path = Path(filename)
    print(f"\n--- Membaca file: {path.name} ---")
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass 
    else:
        print(contents)
        
