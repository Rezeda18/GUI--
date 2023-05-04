from datetime import date
def z12():
    class Restaurant:
        def __init__(self, name, type):
            self.name = name
            self.type = type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.name}, кухня: {self.type}")
        def open_restaurant(self):
            print("Ресторан сейчас открыт")

    newRestaurant = Restaurant("ХочуХарчо", "грузинская")
    print(newRestaurant.name, newRestaurant.type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    newRestaurant2 = Restaurant("TokioCiti", "китайская")
    newRestaurant2.describe_restaurant()

    newRestaurant3 = Restaurant("Бахрома", "француская")
    newRestaurant3.describe_restaurant()

    newRestaurant4 = Restaurant("СупэСтар", "звёздная")
    newRestaurant4.describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, name, type, character):
            self.name = name
            self.type = type
            self.character = character
        def describe_restaurant(self):
            print(f"Название ресторана: {self.name}, кухня: {self.type}, рейтинг: {self.character}")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

        def change(self):
            print("Изначальная оценка ресторана: ", self.character)
            self.character = input("Как вы оцените данный ресторан?: ")
            print("Изменённая оценка ресторана: ", self.character)

    newRestaurant = Restaurant("ХочуХарчо", "грузинская", 3)
    print(newRestaurant.name, newRestaurant.type, newRestaurant.character)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
    newRestaurant.change()
z3()

