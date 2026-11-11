class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        return f"Hello, I am {self.name}, model {self.model}."

class Robot_Dog(Robot):
    def make_sound(self):
        return "Woof!"  

class Robot_Cat(Robot):
    def make_sound(self):
        return "Meow!"

my_robot_dog = Robot_Dog("Rex", "DogModel")
my_robot_cat = Robot_Cat("Whiskers", "CatModel")

print(my_robot_dog.introduce())
print(my_robot_dog.make_sound())
print(my_robot_cat.introduce())
print(my_robot_cat.make_sound())