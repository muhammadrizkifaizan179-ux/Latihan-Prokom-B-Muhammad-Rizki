from exercise_9_12_module1 import users
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