current_users = ['Briliant', 'ghani', 'nur', 'haimin', 'aan']
new_users = ['brilian', 'daffa', 'nur', 'muhammad', 'satriawan']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: you will need to enter a new username.")
    else:
        print(f"{new_user}: this username is available.")