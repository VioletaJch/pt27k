
# Complete the function which returns the weekday according to the input number:
# Otherwise returns "Wrong, please enter a number between 1 and 7"

# def import_number_to_get_weekday(number):
#         weekdays = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
    
#     }
#         return weekdays.get(number, "Wrong, please enter a number between 1 and 7")

# number = int(input("Enter a number (1-7) to get the weekday: "))
# print(import_number_to_get_weekday(number)) # type: ignore

# Number items in the list

# values = ["a", "b", "c"]
# index = 0

# for value in values:
#     print(index, value)
#     index += 1

# values = ["a", "b", "c"]
# for count, value in enumerate(values, start=1):
#     print(count, value)

# Sunumeruotas sarasas, kuris dalinasi is dvienju 

# def even_items(numbers: list) -> list:
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]

# seq = list(range(1, 11))

# print(even_items(seq))

# Grazina sunumeruota sarasa :

# def print_enumerated(numbers):
#     for index, value in enumerate(numbers, start=1):
#         print(f"Item {index}: {value}")

# numbers = [5, 15, 25, 35]
# print_enumerated(numbers)

# zmogaus aprasymas


# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age


#     def say_hello(self) -> None:
#         print(f"{self.name} shouts Hellooo!")

#     def increment_year(self) -> None:
#         self.age = self.age + 1


# person1 = Person("Tom", 40)
# person2 = Person("Antanas", 20)

# person1.say_hello()
# person2.say_hello()

# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def travel(self):
#         print(f"{self.name} is walking..")

#     def say_hello(self):
#         print(f"{self.name} says Hello!")

# class Driver(Person):
#     def _init_(self, name: str, car: str, age: int = 0) -> None:
#         super()._init_(name, age)
#         self.car - car


#     def travel(self):
#         print(f"{self.name} is driving a car.. much faster than walking")

# person1 = Person("Tom", 40)
# person2 = Driver("Antanas", "Opel", 20)

# person1.say_hello()
# person1.travel()
# person2.say_hello()
# person2.travel()

############################################################
        
# class Person:
#     def __init__(self, name: str, age: int = 0) -> None:
#         self.name = name
#         self.age = age

#     def travel(self):
#         print(f"{self.name} is walking...")

#     def say_hello(self):
#         print(f"{self.name} says Hello!")


# class Driver(Person):
#     def __init__(self, name: str, car: str, age: int = 0) -> None:
#         super().__init__(name, age)
#         self.car = car

#     def travel(self):
#         print(f"{self.name} is driving a car and it's {self.car}... much faster than walking")




# person1 = Person("Tom", 40)
# person2 = Driver("Antanas", "Opel", 25)

# person1.say_hello()
# person1.travel()
# person2.say_hello()
# person2.travel()

#############################################################

# 1. Create a Calculator class with main functionality: add, divide, multiply, subtract , 
# etc.. Initiate class and show up some calculations.

# class Calculator:
#     def add(self, a: int, b: int) > float:
#         return a + b
    
#     def subtract(self, a: int, b: int)> float:: 
#         return a - b
    
#     def multiply(self, a: int, b: int) > float::
#         return a * b
    
#     def divide(self, a: int, b: int) -> float:
#         return a / b
    
# calc = Calculator()  

# print("addition: ", calc.add(5, 2))
# print("substractio: ", calc.subtract(7, 3))
# print("multiplication: ", calc.multiply(2, 2))
# print("division: ", calc.divide(10, 2))


# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. 
# Make sure the entire email is in lowercase.

# class Employee:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname
        
#     def full_name(self):
#         return self.name + " " + self.surname
    
#     def e_mail(self):
#         return f"{self.name.lower()}.{self.surname.lower()}@company.com"
    

    
# employee = Employee("Mike", "Jonson")
# print(f"Full name: {employee.full_name()}")
# print(f"e-mail: {employee.e_mail()}")

# Create a Book class that has two attributes:

# title
# author

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author 

       
    def title(self) -> str:
        return self.title
    
    def author(self) -> str:
        return self.author

    def get_title(self) -> str:
        return f"Title: {self.title}"
    
    def get_author(self) -> str:
        return f"Author: {self.author}"
    
book = Book ("Harry Potter","J.K. Rowling")
print(title)
print(author)

print(book.get_title())
print(book.get_author())
# print (f"{book.get_title()}")
    
    



