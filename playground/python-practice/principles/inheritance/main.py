class Animal:

    def sleep(self):
        print("zzzzzz")


class Sheep(Animal):
    def speak(self):
        print("baaaah")


class Dog(Animal):

    def speak(self):
        print("woof")


a = Sheep()

a.sleep()  # inherited
