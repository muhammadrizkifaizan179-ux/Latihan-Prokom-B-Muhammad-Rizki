angka_pertama = input('masukkan angka :')
angka_kedua = input('masukkan angka : ')

try:
    total = int(angka_pertama) + int(angka_kedua)
except ValueError:
    print('maaf, yang anda masukkan bukan angka')
else:
    print(f'hasilnya adalah {total}')