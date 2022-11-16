# Animal is-a object
class Animal(object):
    pass


class Dog(Animal):
    # Dog is-a Animal
    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name
        print(name)

        # Person has-a pet of some kind
        self.pet = None


# Person has-a Employee
class Employee(Person):
    def __init__(self, name, salary):
        # Call super class, in this case Person
        super(Employee, self).__init__(name)
        self.salary = salary
        print(salary)


# mary is-a Person
mary = Person("Mary")
hai = Employee("Hai", 1000)


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")
