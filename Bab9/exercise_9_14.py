from random import sample

pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

winning = sample(pool, 4)

print(f"Tiket yang cocok dengan {winning[0]}, {winning[1]}, "
      f"{winning[2]}, dan {winning[3]} memenangkan hadiah!")