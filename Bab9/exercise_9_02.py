class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Cetak nama restoran dan jenis masakannya."""
        print(f"Nama restoran adalah {self.restaurant_name}")
        print(f"Jenis masakannya adalah {self.cuisine_type}")

    def open_restaurant(self):
        """Cetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka!")


restaurant1 = Restaurant("warung aan", "b2")
restaurant2 = Restaurant("bahasi", "masakan italia")
restaurant3 = Restaurant('tivas, masakan', 'barat')

restaurants = [restaurant1, restaurant2, restaurant3]
for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print('=============================')
    
    