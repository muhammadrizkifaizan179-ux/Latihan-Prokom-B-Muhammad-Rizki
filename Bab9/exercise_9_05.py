class users:
    def __init__(self, first_name, last_name, city, age,):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print(f'nama      : {self.first_name} {self.last_name}')
        print(f'kota asal : {self.city}')
        print(f'umur      : {self.age}')
        
    def greet_user(self):
        print(f'selamat datang {self.first_name}')
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'percobaan login {self.login_attempts} ')
        
    def reset_login_attempt(self):
        self.login_attempts = 0
        print(f'percobaan login {self.login_attempts}')
    
    
    
    
user1 = users('aan', 'briliant', 'magelang', '20')
user2 = users('muhammad', 'daffa', 'solo', '21')
user3 = users('raya', 'barradaeva', 'solo', '20')

pengguna = [user1, user2, user3]
for user in pengguna:
    user.describe_user()
    user.greet_user()
    print('====================')
    
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempt()