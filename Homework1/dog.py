class Dog:
    def __init__(self, name):
        self.hunger = 100
        self.name = name
    def eat(self):
        if self.hunger > 20:
            print(f"{self.name} Not Hungry.")
