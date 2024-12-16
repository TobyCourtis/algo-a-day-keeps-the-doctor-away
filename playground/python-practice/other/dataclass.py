from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None


person = Person(name="John Doe", age=30, email="johndoe@example.com")
person2 = Person(name="John Doe", age=30)
print(person)
print(person.name)
print(person.email)

print(person2.email)
