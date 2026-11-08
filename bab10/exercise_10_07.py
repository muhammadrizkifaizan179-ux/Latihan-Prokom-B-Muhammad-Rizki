print('kalkulator penjumlahan, ketik keluar unyuk berhenti')

while True:
    pertama = input('masukkan angka : ')
    if pertama == 'keluar':
        break
    
    kedua = input('masukkan angka : ')
    if kedua == 'keluar':
        break
    
    try:
        total = int(pertama) + int(kedua)
    except ValueError:
        print('maaf, yang anda masukkan bukan angka')
    else:
        print(f'hasilnya adalah {total}')
        print('=================')