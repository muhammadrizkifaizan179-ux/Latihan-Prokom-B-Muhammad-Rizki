from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/bab10/learning_python.txt')
for line in path.read_text().splitlines():
    modified_line = line.replace('Python', 'C')
    print(modified_line)