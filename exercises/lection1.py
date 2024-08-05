# name = "Code Academy"
# print(name[5])

# # A

# print(name[-2])

# # m

# print(name[5:12])

# # Academy

# print(name[5:])

# # Academy

# print(name[:4])

# # Code

# print(name[5:12:1])

# # Academy

# print(name[5::2])

# # Aaey

# print(name[::-1])

# # ymedacA edoC

# print(name.split())

# # ['Code', 'Academy']

# print(name.upper())

# # CODE ACADEMY

# print(name.replace('c', 'k'))

# # Code Akademy

# a = 5.5
# b = 25.3

# c = a + b 
# print(c)

# c = a - b
# print(c)

# c = a * b
# print(c)

# c = b / a
# print(a)

# c = b // a
# print(a)


# c = a % b
# print(c)

# c = a ** b
# print(c)

# greeting = "Hello, my name is"
# name = input("Please enter your name: ")

# my_list = []

# name = "Tom"
# my_list.append(name)
# my_list.append(name)

# my_list.insert(3, "Vytautas")

# print(my_list)
# print(my_list.count("Vytautas"))

# my_list.remove(my_list[-1])
# print(my_list)
# print(my_list.count("Vytautas"))

# print(len(my_list))

# my_list = [50, 99, 1, -50]
# print(min(my_list))


# my_list = [1, 2, 3, 4, 5,]
# for item in my_list:
#     print(item)

# print("job's done")

# my_list = [1, 2, 3, 50, 30, 17]

# my_list.sort()
# print(my_list)
 
# print("dog" in my_list)

# Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself).

# my_list = [1, 5, 9, 20, 15]
# print(sum(my_list))
      
# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself).

# my_list = [1, 5, 9, 20, 15]
# result = 1
# for item in my_list:
#     result *= item
# print(result)

# Write a python program that gets maximum value from the list (all items are integers or floats in list, create a list yourself)

# my_list = [1, 5, 9, 20, 15]
# print(max(my_list))

# Write a python program that concatenates all strings in the list (all items are strings, create a list yourself).

# my_list = ["suo", "kate", "gyvate"]
# result = "".join(my_list)
# print(result)

# Create two lists and add them together, make sure it works the way you want it to.

# my_list1 = [1, 2, 3]
# my_list2= [4, 5, 6]

# result = my_list1 + my_list2
# print(result)

# Write a python program that asks user to enter 3 integers and find the highest value entered.

# # Prompt the user to enter 3 integers
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# num3 = int(input("Enter the third integer: "))

# # Find the maximum value among the entered integers
# max_value = max(num1, num2, num3)

# # Print the highest value
# print(max_value)

# my_dictionary = {}
# my_dictionary["name"] = "Tom"
# print(my_dictionary["name"])


# 1. Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print it.

# name = str(input("Enter your name: "))
# surname = str(input("Enter your surname: "))
# age = int(input("Enter your age: "))

# my_dictionary = {name, surname, age}
# print(my_dictionary)

# Try creating nested dict structure which would use all data types and structures you already know.

# my_dic = {
#   "name" : name,
#   "surname" : surname,
#   "age" : age
# }
# print(my_dic)

def get_sentences():
    sentences = []