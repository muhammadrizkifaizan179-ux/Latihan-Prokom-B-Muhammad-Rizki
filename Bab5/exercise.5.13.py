import random

angka = random.randint(1, 100)

while True:
    tebakan = int(input("Tebak angka (1-100): "))

    if tebakan < angka:
        print("Terlalu kecil!")
    elif tebakan > angka:
        print("Terlalu besar!")
    else:
        print("Benar!")
        break