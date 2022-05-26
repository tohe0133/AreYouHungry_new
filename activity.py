class Activity:
    def __init__(self, aName, aCoords1, aCoords2, aRating, aPrice):
        self.name = aName
        self.coords1 = aCoords1
        self.coords2 = aCoords2
        self.rating = float(aRating)
        self.price = int(aPrice)

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_price(self):
        return self.price

    def get_coords_x(self):
        return self.coords1

    def get_coords_y(self):
        return self.coords2