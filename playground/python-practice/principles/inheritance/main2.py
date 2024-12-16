from abc import ABC, abstractmethod


class Animal(ABC):
    _name = ""

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("zzzzz")

    @property
    def name(self):
        return self._name


class Dog(Animal):

    def speak(self):
        print("woof")


class Cat(Animal):

    def speak(self):
        print("meow")

    def sleep(self):
        print("meow zzz")


if __name__ == "__main__":
    animals: list[Animal] = [Cat("sam"), Dog("Buzz")]
    d = Dog("Buzz")
    d.speak()
    d.sleep()  # super

    c = Cat("sam")
    c.speak()
    c.sleep()

    for animal in animals:
        animal.sleep()  # polymorphism

    print(d.name)
