class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f"{self.name} їсть.")

    def sleep(self):
        print(f"{self.name} спить.")

    def make_sound(self):
        print(f"{self.name} издає звук.")

    def __str__(self):
        return f"{self.species} на ім'я {self.name}, {self.age} років."


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Собака", age)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} гавкає: Гав")

    def fetch(self):
        print(f"{self.name} приносить палку.")

    def __str__(self):
        return f"{self.species} породи {self.breed} на ім'я {self.name}, {self.age} років."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Кіт", age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} мявкая: Мяу")

    def climb(self):
        print(f"{self.name} лазить по дереву.")

    def __str__(self):
        return f"{self.species} кольору {self.color} на ім'я {self.name}, {self.age} років."



if __name__ == "__main__":
    dog = Dog(name="Штірліц", age=5, breed="Немецька Овчарка")
    cat = Cat(name="Кіт", age=3, color="Рижий")

    print(dog)
    dog.eat()
    dog.make_sound()
    dog.fetch()

    print("\n" + str(cat))
    cat.sleep()
    cat.make_sound()
    cat.climb()