from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract class Person, contains abstract method get_gender"""

    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    """Class Male inheriting class Person"""

    def get_gender(self):
        return "Male"


class Female(Person):
    """Class Female inheriting class Person"""

    def get_gender(self):
        return "Female"


if __name__ == "__main__":
    # try:
    #     person = Person()
    # except TypeError as e:
    #     print(f"Error: {e}")

    male_person = Male()
    female_person = Female()

    print(male_person.get_gender())
    print(female_person.get_gender())
