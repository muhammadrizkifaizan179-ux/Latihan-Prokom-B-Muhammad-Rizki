pizza = ["pepperoni", "keju", "jamur", "ayam bbq", "sosis"]
pizza_aan = pizza[:]
pizza_aan.append("bawang")

print("topping pizza favoritku adalah:")
for toping in pizza:
    print(toping)
    
print("\ntopping pizza favorit temanku adalah:")
for toping in pizza_aan:
    print(toping)