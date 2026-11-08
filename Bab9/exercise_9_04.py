class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serve = 0

    def describe_restaurant(self):
        """Cetak nama restoran dan jenis masakannya."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Cetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")
    
    def set_number_serve(self, number_serve):
        self.number_serve  = number_serve
        print(f'jumlah pelanggan yang dilayani {self.number_serve}')
        
    def increment_number_served(self, increment):
        self.number_serve += increment
        print(f'jumlah pelanggan yang dilayani {self.number_serve}')
        
restaurant = Restaurant('bahari', 'masakan jawa')
    
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_serve(10)
restaurant.increment_number_served(30)

        
        
