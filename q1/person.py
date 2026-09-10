
class Person:

    def __init__(self, pid, surname, given_name, age):
        """Initialize the Person with initial values."""
        self.pid = pid
        self.surname = surname
        self.given_name = given_name
        self.age = age

    def __str__(self):
        """Return a string representation of the Person."""
        return f"{self.surname.title()}, {self.given_name.title()} ({self.pid}) => {self.age} yo"

