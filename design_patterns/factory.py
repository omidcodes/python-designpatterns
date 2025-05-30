"""
Factory Pattern
🔧 Practice: Create an AnimalFactory

Define two animal classes: Dog and Cat with a .speak() method.

Write a factory function get_animal(animal_type) that returns the correct instance.

Add error handling for unsupported types.

🧠 Bonus: Extend it to a factory class instead of a function.
"""

from abc import ABC

class Animal(ABC):

    def speak():
        pass

class Cat(Animal):

    def speak(self):
        print("I am a cat")

class Dog(Animal):

    def speak(self):
        print("I am a dog")


# Factory Function
def get_animal(animal_kind):
    """ Factory Function """

    mapping = {
        "cat" : Cat,
        "dog" : Dog
    }
    animal_object = mapping[animal_kind.strip().lower()]()
    return animal_object



animal1 = get_animal("dog")
animal1.speak()


animal2 = get_animal("cat")
animal2.speak()
