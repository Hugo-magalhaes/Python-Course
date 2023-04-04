class Person:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first}, {self.last}"


def say_my_name(person: Person) -> str:
    return person.full_name
