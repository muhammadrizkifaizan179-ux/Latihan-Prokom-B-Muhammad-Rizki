prompt = "\nmasukkan toping pizza anda(ketik 'quit' untuk keluar):"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"aku akan menambahkan {topping} ke pizza kamu.")