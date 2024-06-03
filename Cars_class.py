'''Class constructors or Object-Oriented Programming (OOP)'''

# Class constructors allow you to create and initialise objects making those object ready to you.
# Class constructors trigger Python's class instantiation process which involves class creation and initialisation.
# Classes can have attributes for sorting data and methods for defining behaviour (similar to functions).
# An instance of a class is an object that belongs to said class
# for examples

class SomeClass:
    pass

# Call the class to construct an object
SomeClass()

# In this example, you define SomeClass using the class keyword. This class is currently empty because it doesnt
# have an attribute or methods as pass has been used as a placeholder.
# Then you create a new instance of SomeClass by calling the class with a pair of parenthese.
# Note, when you call a class, you are calling the class constructor (creator), which creates, initialises and returns
# a new object by triggering Python's internal instantiation process.

"""Instantiation process"""
# Whenever you call a class to create a new instance, there is a two-step process that has to be completed:
# 1. Create a new instance of the target (parent) class
# 2. Initialise the new instance with an appropriate initial state?????

# There are two different dunder methods that be used to create a new instance of a class:
# The first one is __new__() which creates and returns a new empty object.
# The second one is __init__() which takes the resulting object along with the class constructor's
# arguments (therefore, the instance has adopted the parent classes arguments). This method takes
# the new object as its first argument, self. Self takes an attribute (e.g. height, first name, last name etc) and
# initialises the attribute by adopting the arguments of the parent class and creates a new object.
# Click on the link below to watch a short video about this process

#https://www.youtube.com/watch?v=yYALsys-P_w
#https://www.youtube.com/watch?v=pUGyU-hxw5E

# Note, some methods in python receive the self keyword as a parameter, other cls and others nothing at all.
# cls is a keyword used to access a class method
# self is a keyword that is used to access an instance method, which retrieves all the attributes of a class.
# Class methods are called using the decorator @classmethod. They are typically used if you want to create a method
# that is not specifically for an instance (object) of a class. Therefore, think of it as an alternive constructor to
#to create a method before you create an instance. Depending on your task, you might have to create a class method that
#preceeds any instance.
# It is possible to create a class attributes which remains true for each instance. However, instance attributes are
# changeable.

"""Dunders in Pyhton"""

#__dict__
# Dunder dict is used to present all attributes in an object. See below example where attributes of an instance were printed

#jess_car.__dict__
funho = {'make': 'BMW', 'colour': 'silver', 'doors': 5, 'parked': True, 'clean': True}


class Cars:
    total_cars_at_Sa_Dias_residence: int = 0

    def __init__(self, make: str, colour: str, doors: int):
        self.make = make
        self.colour = colour
        self.doors = doors
        self.parked = True
        self.clean = True
        self.faulty_brakes = False
        Cars.add_car()

    def __str__(self):
        return f"A {self.colour} {self.make} car that has {self.doors} doors. Very chic!"

    @classmethod
    def get_number_of_household_cars(cls):
        return cls.total_cars_at_Sa_Dias_residence
    @classmethod
    def add_car(cls):
        cls.total_cars_at_Sa_Dias_residence += 1
        #Separation of concerns!

    def drive(self, location: str):
        self.clean = False
        if location == 'car wash':
            print(f'I am going to take my {self.colour} {self.doors}-door {self.make} car to the car wash!')
        if location != 'car wash':
            print(f'I am going to drive my {self.colour} {self.doors}-door {self.make} car to {location}.')
        if location == 'Southend':
            self.faulty_brakes = True
            print('Shit! Almost caused a collision! I need to book a MOT test NOW.')
        if location == 'MOT test centre':
            self.faulty_brakes = False
            print("Thank you for fixing my brakes sir! Skrr skrr.")
        if self.faulty_brakes == True and location != 'MOT test centre' and location != 'car wash':
            print(f'Damn! I need to drive to the nearest MOT test centre immediately instead of driving to {location} '
                  f' with faulty brakes!')





    def car_wash(self):
        if self.clean == False:
            self.drive('car wash')
            self.parked = False
            self.clean = True
            return
        print(f'I am going to take my {self.colour} {self.doors}-door {self.make} car to the car wash!')

    def drive_home(self):
        if self.clean == True:
            print(
                f'Now that my {self.colour} {self.doors}-door {self.make} '
                f' car is clean, I am going to drive home and do some coding.')
            self.parked = True
            self.clean = True


class ElectricCars(Cars):
    def __init__(self, make: str, colour: str, doors: int):
        super().__init__(make, colour, doors)
        self.electric = True

    def __str__(self):
        return (f"A {self.colour} {self.make} car that has {self.doors} doors."
                f" What a beaut she is... And she's electric")

    def is_electric_car(self):
        if self.electric == True:
            print("There is an electrical current travelling through my vehicle!")
        if self.electric == False:
            print("Oh hell naw! My car doesn't run on electricity?!")

    def charge_electric_car(self):
        if self.electric == True:
            print("I need more power!!! I better charge this bad boy before the battery is kaput!")

        if self.electric == False:
            print("Oh yeah, I have an air pollutant... Sigh, I guess I should drive to the nearest petrol station :(")

    def charge_car(self):
        if self.electric == True and self.faulty_brakes == False:
            print("I need more power. I better charge this bad boy before the battery is kaput!")
        if self.faulty_brakes == True:
            print(f"I can't charge my car yet because my car has faulty brakes!"
                  f" I need to drive to the nearest MOT test centre immediately!")

    def need_petrol(self):
        if self.electric == False and self.faulty_brakes == False:
            print("Oh yeah, I have an air pollutant... Sigh, I guess I should drive to the nearest petrol station :(")
        if self.faulty_brakes == True:
            print(f"I can't get petrol yet because my car has faulty brakes!"
                  f" I need to drive to the nearest MOT test centre immediately!")
def main():
    print("Cars_class's main method")
if __name__ == '__main__':
    main()

# nevah_car = ElectricCars('Mercedes', 'turquoise', 10)
#
# timmy_car = ElectricCars('Smart', 'yellow', 3)
#
# jess_car = Cars('BMW', 'red', 9)
#
# pedro_car = Cars('BMW', 'red', 9)

# print(nevah_car)
# print(timmy_car)
# print(jess_car)
# print(pedro_car)

# print(Cars.get_number_of_household_cars())
# nevah_car.drive('Battersea')
# print(nevah_car.clean)
# nevah_car.car_wash()
# print(nevah_car.clean)
# nevah_car.car_wash()
# nevah_car.drive('Southend')
# nevah_car.drive('Scotland')
# nevah_car.drive('MOT test centre')
# nevah_car.car_wash()
# nevah_car.charge_car()
# nevah_car.drive_home()
# print(vars(nevah_car))

# print(jess_car.get_number_of_household_cars()) #1
# print(jess_car.total_cars_at_Sa_Dias_residence) #1
#
# jess_car.add_car()
# print(jess_car.get_number_of_household_cars()) #2
#
# #cls.total_cars_at_Sa_Dias_residence += 1
# jess_car.total_cars_at_Sa_Dias_residence = Cars.total_cars_at_Sa_Dias_residence + 1



# print(jess_car.total_cars_at_Sa_Dias_residence) #3
# print(type(jess_car.get_number_of_household_cars)) #2
# print(type(jess_car.drive('Clapton'))) #2

# print(Cars.get_number_of_household_cars()) #2
# print(Cars.get_number_of_household_cars()) #1
# # print(jess_car.total_cars_at_Sa_Dias_residence)
# #
# #
# #
# #
# #
# print(pedro_car.total_cars_at_Sa_Dias_residence) #1
# print(Cars.total_cars_at_Sa_Dias_residence) #1
# pedro_car.total_cars_at_Sa_Dias_residence += 1
# print(pedro_car.total_cars_at_Sa_Dias_residence) #2
# print(Cars.total_cars_at_Sa_Dias_residence) #1
#
#


