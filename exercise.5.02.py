mobil = 'subaru'
mobil_mobil = ['subaru', 'audi', 'bmw', 'toyota']
merek = 'Audi'
umur = 18

# --- Kesamaan dan ketidaksamaan string ---
print("apakah mobilnya == 'subaru'? aku memprdiksi true.")
print(mobil == 'subaru')

print("\nApakah mobil == 'audi'? aku memprediksi false.")
print(mobil == 'audi')

print("\nApakah mobil != 'audi'? aku memprediksi true.")
print(mobil != 'audi')

print("\nApakah mobil != 'subaru'? aku memprediksi false.")
print(mobil != 'subaru')

# --- Tes dengan lower() ---
print("\nApakah merek.lower() == 'audi'? aku memprediksi true.")
print(merek.lower() == 'audi')

print("\nApakah merek.lower() == 'Audi'? aku memprediksi false.")
print(merek.lower() == 'Audi')

# --- Tes angka ---
print("\nApakah umur == 18? aku memprediksi true.")
print(umur == 18)

print("\nApakah umur == 21? aku memprediksi false.")
print(umur == 21)

print("\nApakah umur != 21? aku memprediksi true.")
print(umur != 21)

print("\nApakah umur != 18? aku memprediksi false.")
print(umur != 18)

print("\nApakah umur > 17? aku memprediksi true.")
print(umur > 17)

print("\nApakah umur > 18? aku memprediksi false.")
print(umur > 18)

print("\nApakah umur < 21? aku memprediksi true.")
print(umur < 21)

print("\nApakah umur < 18? aku memprediksi false.")
print(umur < 18)

print("\nApakah umur >= 18? aku memprediksi true.")
print(umur >= 18)

print("\nApakah umur >= 19? aku memprediksi false.")
print(umur >= 19)

print("\nApakah umur <= 18? aku memprediksi true.")
print(umur <= 18)

print("\nApakah umur <= 17? aku memprediksi false.")
print(umur <= 17)

# --- Kata kunci and dan or ---
print("\nApakah umur >= 18 and umur < 21? aku memprediksi true.")
print(umur >= 18 and umur < 21)

print("\nApakah umur > 20 and umur < 30? aku memprediksi false.")
print(umur > 20 and umur < 30)

print("\nApakah umur < 10 or umur > 15? aku memprediksi true.")
print(umur < 10 or umur > 15)

print("\nApakah umur < 10 or umur > 20? aku memprediksi false.")
print(umur < 10 or umur > 20)

# --- Item ada di dalam list ---
print("\nApakah 'audi' in mobil_mobil? aku memprediksi true.")
print('audi' in mobil_mobil)

print("\nApakah 'honda' in mobil_mobil? aku memprediksi false.")
print('honda' in mobil_mobil)

# --- Item tidak ada di dalam list ---
print("\nApakah 'honda' not in mobil_mobil? aku memprediksi true.")
print('honda' not in mobil_mobil)

print("\nApakah 'audi' not in mobil_mobil? aku memprediksi false.")
print('audi' not in mobil_mobil)