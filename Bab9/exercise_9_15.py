from random import sample

pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

my_ticket = (3, 7, 'a', 'c')

attempts = 0
while True:
    attempts += 1
    draw = sample(pool, 4)
    if set(draw) == set(my_ticket):
        break

print(f"Butuh {attempts} kali undian sampai tiketmu menang.")