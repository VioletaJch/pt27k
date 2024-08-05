# Find all of the numbers from 1-1000 that are divisible by 6.


# 3. Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

# text = "A child sits on the tree and sees how an applee falls down"

# words = text.split()

# answer = [word for word in words if "e" in word]
# print(answer)


# 4. Given the same string as in previous exercise: calculate count of words that have more than 5 characters.

# text = "A child sits on the tree and sees how an applee falls down"

# words = text.split()

# answer = [word for word in words if len(word) > 4] 

# for word in answer:

#     print(f"{word}: {len(word)}")

# 5. Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# from collections import Counter

# def count_letter_occurrences(s):
#     """Counts the occurrence of each letter in the given string."""
#     # Convert the string to lowercase and filter only alphabetic characters
#     filtered_string = ''.join(char.lower() for char in s if char.isalpha())
    
#     # Use Counter to count occurrences of each letter
#     return Counter(filtered_string)

# # Example usage
# input_string = "A child sits on the tree and sees how an apple falls down"
# result = count_letter_occurrences(input_string)

# # Print the results
# print("Letter occurrences in the given string:")
# for letter, count in result.items():
#     print(f"{letter}: {count}")

#  Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# 6.  Write a program that checks if given number is a perfect square.

# 1)

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# my_list = list(text)

# print(f"my_list:\n{my_list}")

# occurences = {letter: my_list.count(letter) for letter in my_list if letter != " " and letter != "-" and letter != "."}

# print(occurences)

# 2)

# import math

# def is_perfect_square(n):
#     """Check if a number is a perfect square."""
#     if n < 0:
#         return False
#     root = math.isqrt(n)  # Compute the integer square root
#     return root * root == n

# # Example usage
# number = int(input("Enter a number to check if it's a perfect square: "))
# if is_perfect_square(number):
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")

# 3)

# def is_square(n):
#     return int(n**0.5) ** 2 == n

# user_input = int(input("Please insert a number "))
# print(is_square(user_input))


# print perfect squares in range 10

# 1)

# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)

# 2)

# squares = [number * number for number in range(10)]
# print(squares)

# def import_number_to_get_weekday(number):

#     weekdays = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
    
#     }

#     return weekdays.get(number, "Wrong, please enter a number between 1 and 7")

# number = int(input("Enter a number (1-7) to get the weekday: "))
# print(import_number_to_get_weekday(number))

# Dictionary comprehensions

# 1)

# list = {1: 1, 2: 4, 3: 9}
# squares = {i: i * i for i in list}
# print(squares)

# 2)

# squares = {i: i * i for i in range(10) if i != 5}
# print(squares)

# 3)

# squares = {i: i * i for i in range(10) if i % 2 == 0}
# print(squares)

# Complete the function which returns the weekday according to the input number:
# Otherwise returns "Wrong, please enter a number between 1 and 7"


