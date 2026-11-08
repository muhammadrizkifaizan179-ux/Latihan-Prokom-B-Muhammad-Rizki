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

class privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privilage(self):
        print('admin berhak untuk: ')
        for hak in self.privileges:
            print(f'{hak}')
            
class admins(users):
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privileges = privileges()
        
admin = admins('muhammad', 'rizki', 'solo', '18')
admin.describe_user()
admin.privileges.show_privilage()