bahasa_favorit = { 'rizki' : 'inggris',
                  'aan' : 'arab',
                  'dito' : 'jepang',
                  'daffa' : 'jawa'}
orang = ['kayla', 'nayla', 'briliant', 'aan', 'dito,']

for peserta in orang:
    if peserta in bahasa_favorit:
        print(f"Terima kasih sudah merespon, {peserta.title()}!")
    else:
        print(f"{peserta.title()}, tolong isi poll kita!")