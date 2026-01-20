#1.	Write a program that generates a set of prime numbers and another set of odd numbers. 
# Demonstrate the result of union,intersection, difference, and symmetric difference operations on these sets.
set1 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
set2 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
print("Set of prime numbers:", set1)
print("Set of odd numbers:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Difference (Set2 - Set1):", set2.difference(set1))
print("Symmetric Difference:", set1.symmetric_difference(set2))

#2.	Write a program that creates two sets. One of even number in range 1-10 and the other has all composite numbers in range 1-20.
#  Demonstrate the use of all(), isuperset(), len(), sum(), update(), pop(), remove(), add() and clear() functions on sets.
set1 = {2, 4, 6, 8, 10}
set2 = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}
print("Set of even numbers:", set1)
print("Set of composite numbers:", set2)
print("All elements in set1 are even:", all(x % 2 == 0 for x in set1))
print("Set1 is superset of Set2:", set1.issuperset(set2))
print("Length of Set1:", len(set1))
print("Sum of elements in Set1:", sum(set1))
print("Set1 before update:", set1)
set1.update(set2)
print("Set1 after update:", set1)
if set1: 
    print("Set1 before pop:", set1)
    popped_element = set1.pop()
    print("Popped element:", popped_element)
    print("Set1 after pop:", set1)
if popped_element in set1: 
    print("Set1 before remove:", set1)
    set1.remove(popped_element)
    print("Set1 after remove:", set1)
print("Set1 before add:", set1)
set1.add(12)
print("Set1 after add:", set1)
print("Set1 before clear:", set1)
set1.clear()
print("Set1 after clear:", set1)

#3.	Write a Python program to check if a given value is present in a set or not.
set1 = {1, 2, 3, 4, 5}
value = 6
if value in set1:
    print(f"{value} is present in the set.")
else:
    print(f"{value} is not present in the set.")
#4.	WAP to access values stored in a dict, add a new item in the dict,
#  modify an item in the dict, remove an element from dict.
dict1 = {"name": "ved", "age": 19, "city": "New York"}
print("Original dictionary:", dict1)
print("Accessing values in dictionary:")
for key, value in dict1.items():
    print(f"{key}: {value}")

dict1["country"] = "USA"
print("Dictionary after adding new item:", dict1)

#5.	WAP to access items in a dictionary using for loop.

dict1 = {"name": "ved", "age": 19, "city": "New York"}
print("Accessing items in dictionary using for loop:")
for key, value in dict1.items():
    print(f"{key}: {value}")

#6.	WAP to demonstrate the use of various in-built functions in dictionary.
dict1 = {"name": "ved", "age": 19, "city": "New York"}
print("Original dictionary:", dict1)
print("Keys:", dict1.keys())
print("Values:", dict1.values())
print("Items:", dict1.items())
print("Length of dictionary:", len(dict1))
print("Dictionary after clearing:", dict1.clear())
print("Dictionary after clearing:", dict1)
dict_copy = {"name": "ved", "age": 19, "city": "New York"}
print("Dictionary after copying:", dict_copy.copy())
print("Dictionary after copying:", dict_copy)
if dict_copy:
    print("Dictionary after popping item:", dict_copy.popitem())
    print("Dictionary after popping item:", dict_copy)
else:
    print("Cannot pop item from an empty dictionary.")
print("Dictionary after updating:", dict1.update({"name": "ved", "age": 19, "city": "New York"}))
print("Dictionary after updating:", dict1)

#7.	WAP that combines the lists to a dictionary using zip function
list1 = ["name", "age", "city"]
list2 = ["ved", 19, "New York"]
dict1 = dict(zip(list1, list2))
print("Combined dictionary:", dict1)

#8.	Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
#  and the values are the square of the keys.
dict1 = {x: x ** 2 for x in range(1, 16)}
print("Dictionary with keys as numbers and values as squares:", dict1)

#9.	WAP that creates a dictionary of radius of a circle and its circumference.
dict1 = {}
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
dict1["radius"] = radius
dict1["circumference"] = circumference
print("Dictionary with radius and circumference:", dict1)

#10.WAP that creates a dictionary of cubes of odd numbers in the range 1 to 10 using dictionary comprehensions.
dict1 = {x: x ** 3 for x in range(1, 11) if x % 2 != 0}
print("Dictionary with cubes of odd numbers:", dict1)

#11.WAP that has dictionary of names of students and a list of their marks in 4 subjects.
#  Create another dictionary from this dict that has names of the students and their total marks. Find out the topper and his/her score.
dict1 = {
    "Alice": [85, 90, 78, 92],
    "Bob": [75, 80, 88, 70],
    "Charlie": [95, 100, 98, 97]
}
total_marks = {name: sum(marks) for name, marks in dict1.items()}
print("Total marks of students:", total_marks)
topper = max(total_marks, key=total_marks.get)
top_score = total_marks[topper]
print(f"Topper: {topper}, Score: {top_score}")

#12.WAP that prints histogram of frequencies of characters occurring in a message.

message = "hello world"
histogram = {}
for char in message:
    if char.isalpha():
        histogram[char] = histogram.get(char, 0) + 1
print("Histogram of frequencies of characters:")
for char, freq in histogram.items():
    print(f"{char}: {'*' * freq}")

#13.	WAP that displays information about an employee. Use nested dictionary to do the task.
#  Also determine how to access an element in a nested dictionary and how to add an element in nested dictionary.
dict1 = {
    "employee": {
        "name": "harsh patel",
        "age": 20,
        "department": "HR",
        "salary": 50000
    }
}
print("Employee information:")
for key, value in dict1["employee"].items():
    print(f"{key}: {value}")

dict1["employee"]["address"] = "123 Main St, Cityville"
print("Employee information after adding address:")
for key, value in dict1["employee"].items():
    print(f"{key}: {value}")

#14.	Write a program that keeps name and phone numbers in a dictionary as key-value pairs.
#The program should display a menu that lets the user search a person’s phone, add a new name and phone number,
#change an existing phone number, and delete an existing name and phone number.

def display_menu():
    print("\nPhonebook Menu:")
    print("1. Search for a phone number")
    print("2. Add a new contact")
    print("3. Update an existing contact")
    print("4. Delete a contact")
    print("5. Exit")
dict1 = {}
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the name to search: ")
        if name in dict1:
            print(f"{name}'s phone number is {dict1[name]}")
        else:
            print(f"{name} not found in the phonebook.")

    elif choice == "2":
        name = input("Enter the name to add: ")
        if name in dict1:
            print(f"{name} already exists in the phonebook.")
        else:
            phone = input("Enter the phone number: ")
            dict1[name] = phone
            print(f"{name} added successfully.")

    elif choice == "3":
        name = input("Enter the name to update: ")
        if name in dict1:
            phone = input("Enter the new phone number: ")
            dict1[name] = phone
            print(f"{name}'s phone number updated successfully.")
        else:
            print(f"{name} not found in the phonebook.")

    elif choice == "4":
        name = input("Enter the name to delete: ")
        if name in dict1:
            del dict1[name]
            print(f"{name} deleted successfully.")
        else:
            print(f"{name} not found in the phonebook.")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
    name = "ved"