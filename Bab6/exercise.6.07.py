teman_1 ={'first_name' : 'Briliant',
       'last_name'  : 'Ghani',
       'age'        : '90',
       'city'       : 'magelang'}

teman_2 ={'first_name' : 'muhammad',
          'last_name' : 'daffa',
          'age' : '100',
          'city' : 'surakarta'}

teman_3 ={'first_name' : 'muhammad',
          'last_name' : 'Rizki',
          'age' : '18',
          'city' : 'Bandung'}

teman_teman = [teman_1,teman_2,teman_3]

for teman in teman_teman:
    full_name = f"{teman['first_name']} {teman['last_name']}"
    print(f"Name: {full_name}")
    print(f"Age: {teman['age']}")
    print(f"City: {teman['city']}")
    print()