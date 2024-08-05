# Funkcijos

# def print_smth():
#     print('Hello world!')

# print_smth()    


# gauti betkoki skaiciu nuo 1 iki 10

# import random

# def get_random_number():
#     print (random.randint(0, 10))

# get_random_number()


# 1. Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

# 1)


# def find_max(num1, num2, num3):
#     # Returns the maximum of three numbers.
#     return max(num1, num2, num3)

# # Example usage
# print("Maximum:", find_max(7, 2, 5))


# 2)

# def add_two_int_numbers(a: int, b: int) -> int:
#   return a + b

# result = add_two_int_numbers(9, 10)
# print("Sum:", result)

# 3)

# def integer_division(num_one, num_two):
#     return num_one // num_two

# result = integer_division(10, 2)
# print("integer_division(10,2)", result)

# 4)

# def even_odd(num):

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"
    
# result = even_odd(8)
# print(result)


# 2. Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.

# def add_ending_to_list(strings: list, ending: str) -> list:
#     """Adds a specified ending to each string in the list."""
#     return [s + ending for s in strings]

# # Example usage
# strings_list = ["apple", "banana", "cherry"]
# ending = " fruit"
# modified_list = add_ending_to_list(strings_list, ending)
# print("Modified list:", modified_list)

# 3. Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

import random

def get_random_numbers_and_sum_subtract_divide_multiply():
    # Generate two random integers between 0 and 20
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    # Print the two random integers
    print(f"Random number 1: {a}")
    print(f"Random number 2: {b}")

    # Calculate their sum, difference, quotient, and product
    sum_ab = a + b
    diff_ab = a - b
    prod_ab = a * b
    div_ab = a // b

    return sum_ab, diff_ab, div_ab, prod_ab

# Call the function and get the results
result = get_random_numbers_and_sum_subtract_divide_multiply()

# Print the results
sum_ab, diff_ab, div_ab, prod_ab = result
print(f"Sum: {sum_ab}")
print(f"Difference: {diff_ab}")
print(f"Quotient: {div_ab}")
print(f"Product: {prod_ab}")



