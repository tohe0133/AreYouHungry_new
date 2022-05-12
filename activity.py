class Activity:
    def __init__(self, aName, aDistance, aRating, aPrice):
        self.name = aName
        self.distance = float(aDistance)
        self.rating = float(aRating)
        self.price = aPrice

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