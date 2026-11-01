favorite_numbers = {'daffa' : [9, 10] ,
                    'otid'  : [5, 13],
                    'aan'   : [7, 9],
                    'rizki' : [8],
                    'kayla' : [4, 8, 9],}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")