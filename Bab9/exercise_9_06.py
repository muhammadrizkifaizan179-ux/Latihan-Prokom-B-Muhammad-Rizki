class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Cetak nama restoran dan jenis masakannya."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Cetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")

restaurant = Restaurant("Warung Soto Pak Joko", "Masakan Jawa")


class icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanila', 'coklat', 'stroberi']
    def show_flavors(self):
        print(f"Rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")
       
stand = icecreamstand('Es Krim Bahari', 'es krim')
stand.describe_restaurant()
stand.show_flavors()