from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/bab10/learning_python.txt')

print("--- Membaca Seluruh File Sekaligus ---")
contents = path.read_text()
print(contents)

print("--- Membaca Melalui List dan Looping ---")
for line in path.read_text().splitlines():
    print(line)