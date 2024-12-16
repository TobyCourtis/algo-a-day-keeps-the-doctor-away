from typing import List
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("zzzzzz")


class Sheep(Animal):
    def speak(self):
        print("baaaah")


class Dog(Animal):

    def speak(self):
        print("woof")


animals: List[Animal] = [Sheep(), Dog()]

for a in animals:  # polymorphism, subclasses referred to as superclasses
    a.speak()
