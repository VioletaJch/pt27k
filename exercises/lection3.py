# score = int(input("Score: "))
 
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


    # ENDLES LOOP

# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input):
#         break
# print(f"You entered {user_input }")

# 1.  Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = input("please enter your name: ")
# surname = input("please enter your surname")
# age = int(input("please enter your age: "))

# my_dic = {
#     "name": name,
#     "surname": surname,
#     "age": age
# }

# if my_dic["age"] > 21:
#     print("allowed to enter")

# 2. Create a database (list of privileged users), print a specific message with a personal greeting if the user is a privileged and 
# just "Welcome otherwise"

# privileged = ["Violeta", "Mindaugas", "Andrius", "Gabriele"]
# name1 = input("please enter your name: ")

# if name1 in privileged:
#     print("greeting")
# else:
#     print("Welcome otherwise")

# 3. Allow user to enter two numbers, print out which one is higher than the other, or equal.

# number1 = int(input("enter first number "))
# number2 = int(input("enter second number "))

# if number1 > number2:
#     print(f"{number1} is higher than {number2}")

# elif number1 == number2:
#    print(f"{number1} is equal {number2}")
          
# else:
#     print(f"{number1} is lower than {number2}")

# 4. Write a small calculator application, that allows user to enter two numbers and a symbol, do the operation and print the answer.

# number1 = int(input("Please insert first number "))
# number2 = int(input("Please insert second number "))
# operator = input("Please insert an operator for the equation (+, -, * or /) ")
 
# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2
# elif operator == '*':
#     result = number1 * number2
# else:
#     result = number1 / number2
# print(f"{number1} {operator} {number2} = {result}")

# 5. Create a number guessing game from 1-10

# 1)

# number1 = int(input("please enter number 1 to 10: "))
# correct_nu = [5]

# if number1 == correct_nu:
#     print("you are lucky")

# else:
#     print("wrong answer")
 

# 2)

# correct_nu = 5  

# while True:
#     number1 = int(input("Please enter a number between 1 and 10: "))
    
#     if number1 == correct_nu:
#         print("You are lucky!")
#         break
#     else:
#         print("Wrong answer, try again.")

# 8 lection 

# name = "Code Academy"
# for character in name :
#     print(character)


# 8. Print dict items using for 

# my_dict = {"name": "Albert", "role": "scientist"}

# for key, value in my_dict.items():
#     print(key, value)

# 8. Print word for each name in the list 

# names = ("Albert", "Tom", "Leonardo")
# for name in names:
#     print(f"Greetings, {name}")

# Skaiciu seka nuo iki paskutinio

# x = range(3, 6)
# for n in x:
#   print(n)

# atprintina nuo 0 iki nurodyto skaičiaus

# for n in range(10):
#   print(n)

# Skaičių seka iki nurodyto skaičiaus, bet susitojant ties norimu skaičiumi

# i = 1
# while i < 6:
#   print(i)
#   if i == 4:
#     break
#   i += 1

# loop 1. Create a variables containing strings for username and password. Start endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# username = "Tom"
# password = "securepass"
# attempts = 3
 
# while True:
#     print(f"attempts {attempts}")
#     login = input("Insert your username - " )
#     psw = input("Insert your password - ")
#     if login == username and psw == password:
#         print(f"Welcome back {username}")
#         break

#     else:
#         attempts -= 1
#         if attempts > 0:
#             print("Login credentials you've inserted is incorrect, please try again")
#         else:
#             print("try again in 5 minutes")
#             break

# 2. Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

# numbers = []

# while True:
#     user_input = input("Enter 10 integers separated by spaces: ")
#     # Split the input string into individual elements and try to convert them to integers
#     try:
#         numbers = [int(x) for x in user_input.split()]
#     except ValueError:
#         print("Invalid input. Please enter integers only.")
#         continue


#     # Check if the user has entered exactly 10 integers
#     if len(numbers) < 10:
#         print("You have entered less than 10 integers. Please try again.")
#     elif len(numbers) > 10:
#         print("You have entered more than 10 integers. Please try again.")
#     else:
#         break

# average = sum(numbers) / len(numbers)
# sum = sum(numbers)

# # Print the list of integers, counts, and average
# print("The list of entered integers is:", numbers)
# print("Average of the integers:", average)
# print ("Sum of entered integers:", sum)

# 3. Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo
# skaičiaus vertė nuo 1 iki 100.

# import random

# # Generate dictionary with keys 1 to 10 and random values from 1 to 100
# random_dict = {key: random.randint(1, 100) for key in range(1, 11)}

# # Print the generated dictionary
# print(random_dict)

# 4. Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. Reikšmę 
# galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.

# import random

# pin = int(input("please enter 4 digit code: "))

# while True:
#     cracker = random.randint(1000,9999)
#     if cracker != pin:
#         print(f"pin {cracker} is incorrect")

#     else:
#         print(f"the pin is {cracker} you have succesfully cracked the code")
#         break

# Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį. 
# Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.

def calculate_average():
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")

        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")

    if numbers:
        average = sum(numbers) / len(numbers)
        print("\nList of numbers entered:", numbers)
        print("Average of the numbers:", average)
    else:
        print("No numbers were entered.")

# Call the function to run the program
calculate_average()

# def find_sum(num1, num2):
#     '''Returns the sum of num1 and num2.'''
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers