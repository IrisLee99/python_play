class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello, I am {self.name}, model {self.model}.")

class Robot_Dog(Robot):
    def introduce(self):
        super().introduce()
        return f"Hello, I am {self.name}, model {self.model}. Woof!"

class Robot_Cat(Robot):
    def introduce(self):
        super().introduce()
        return f"Hello, I am {self.name}, model {self.model}. Meow!"

my_robot_dog = Robot_Dog("Rex", "DogModel")
my_robot_cat = Robot_Cat("Whiskers", "CatModel")

print(my_robot_dog.introduce())
print(my_robot_cat.introduce())