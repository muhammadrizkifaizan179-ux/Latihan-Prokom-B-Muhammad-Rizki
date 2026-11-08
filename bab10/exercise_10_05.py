from pathlib import Path

path = Path('Latihan-Prokom-B-Muhammad-Rizki/bab10/guest_book.txt')
with path.open('w') as file_object:
    while True:
        name = input("Masukkan nama Anda(ketik keluar untuk berhenti memasukkan nama): ")
        
        if name.lower() == 'keluar':
            print("\nTerima kasih! Buku tamu telah disimpan.")
            break
        
        file_object.write(f"{name}\n")
        print(f"Selamat datang, {name}! Nama Anda telah dicatat.")
        print('========================')
        