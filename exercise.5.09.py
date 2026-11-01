usernames =[]

if usernames:
    for username in usernames:
     if username == 'admin':
        print('Hello admin, would you like to see a status report?')
     else:
        print(f'Hello {username.title()}, thank you for login again')
else:
    print('we need to found new user')