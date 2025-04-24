class Recipe():
    def __init__(self, id, title, cooking_time, rating):
        self.id = id
        self.title = title
        self.cooking_time = cooking_time
        self.rating = rating

    def __repr__(self):
        return f"Recipe({self.id}, {self.title}, {self.cooking_time}, {self.rating})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__