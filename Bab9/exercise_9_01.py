class Restaurant:
    """Model sederhana sebuah restoran."""

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

restaurant.describe_restaurant()
restaurant.open_restaurant()