"""
Factory Pattern
🔧 Practice: Create an AnimalFactory

Define two animal classes: Dog and Cat with a .speak() method.

Write a factory function get_animal(animal_type) that returns the correct instance.

Add error handling for unsupported types.

🧠 Bonus: Extend it to a factory class instead of a function.
"""

from abc import ABC, abstractmethod
from typing import Type

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):

    def speak(self):
        print("I am a cat")

class Dog(Animal):

    def speak(self):
        print("I am a dog")


# Factory Class
class AnimalFactory:

    def __init__(self, animal_kind :str):

        mapping = {
            "cat" : Cat,
            "dog" : Dog
        }
        self._animal_class : Type[Animal] = mapping[animal_kind.strip().lower()]

    def create(self) -> Type[Animal]:
        return self._animal_class()


animal1 = AnimalFactory("dog").create()
animal1.speak()


animal2 = AnimalFactory("cat").create()
animal2.speak()
