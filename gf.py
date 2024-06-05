class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def get_age(self):
        return self._age

    @age.setter
    def get_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age