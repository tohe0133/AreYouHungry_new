class Activity:
    def __init__(self, aName, aDistance, aRating, aPrice, aCoords1, aCoords2):
        self.name = aName
        self.distance = float(aDistance)
        self.rating = float(aRating)
        self.price = aPrice
        self.coords1 = aCoords1
        self.coords2 = aCoords2

    def show_activity_info(self):
        return f"{self.name.title()} is {self.distance} km away it has a rating of {self.rating} and is in a " \
               f"{self.price} price range"

    def get_name(self):
        return self.name

    def get_distance(self):
        return self.distance

    def get_rating(self):
        return self.rating

    def get_price(self):
        return self.price

    def get_price_int(self):
        if self.price == " Free":
            return 0
        elif self.price == " Low":
            return 1
        elif self.price == " Medium":
            return 2
        else:
            return 3

    def get_coords(self):
        return f"{self.coords1},{self.coords2}"

    def get_coords_x(self):
        return self.coords1

    def get_coords_y(self):
        return self.coords2