peliharaan_1 = {'hewan' : 'anjing', 'nama' : 'guguk', 'pemilik' : 'otid'}
peliharaan_2 = {'hewan' : 'kucing', 'nama' : 'miu', 'pemilik' : 'daffa'}
peliharaan_3 = {'hewan' : 'ikan', 'nama' : 'koki', 'pemilik' : 'Rizki'}

peliharaan = [peliharaan_1, peliharaan_2, peliharaan_3]
for hewan in peliharaan:
    print(f"{hewan['nama'].title()} adalah {hewan['hewan']} yang dipelihara {hewan['pemilik'].title()}.")
