file_name ='text_bab_10/learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    
for line in contents.splitlines():
    print(line)