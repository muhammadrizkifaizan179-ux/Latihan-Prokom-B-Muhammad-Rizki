class users:
    def __init__(self, first_name, last_name, city, age):
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