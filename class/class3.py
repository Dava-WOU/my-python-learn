# inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
          
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

mouse.speak()