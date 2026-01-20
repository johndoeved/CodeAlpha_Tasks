# lab 6 Exercise practice
# 1)WAP to swap two values using tuple assignment.
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple1, tuple2 = tuple2, tuple1
print(f"Tuple 1 after swapping: {tuple1}")
# 2)WAP using a function that returns the area and circumference of a circle whose radius is passed as an argument.
def circle_properties(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference
radius=float(input("Enter the radius of the circle: "))
area, circumference = circle_properties(radius)
print(f"Area of the circle and circumference: {area},{circumference}")
# 3).WAP that prints all consonants in a string using list comprehension.
def consonants_in_string(s):
    vowels = "aeiouAEIOU"
    return [char for char in s if char.isalpha() and char not in vowels]
s = input("Enter a string: ")
consonants = consonants_in_string(s)
print(f"Consonants in the string: {consonants}")

#4)WAP that reverse a list using a loop.
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list
#5)WAP to find whether a particular element is present in the list using a loop.
def is_element_present(lst, element):
    for i in lst:
        if i == element:
            return True
    return False
#6)WAP that prints all consonants in a string using list comprehension.
def consonants_in_string(s):
    vowels = "aeiouAEIOU"
    return [char for char in s if char.isalpha() and char not in vowels]
s = input("Enter a string: ")
consonants = consonants_in_string(s)
print(f"Consonants in the string: {consonants}")
#7)WAP that counts the number of times a value appears in the list. Use a loop to do the same.
def count_occurrences(lst, value):
    count = 0
    for i in lst:
        if i == value:
            count += 1
    return count
lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
value = 1
count = count_occurrences(lst, value)
print(f"The value {value} appears {count} times in the list.")
#8)WAP to insert a value in the list at the specified location using while loop.
def insert_value_at_location(lst, value, location):
    lst.insert(location, value)
    return lst
lst = [1, 2, 3, 4, 5]
value = 10
location = 2
lst = insert_value_at_location(lst, value, location)
print(f"List after inserting {value} at location {location}: {lst}")
#9)WAP to transpose two matrices.
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)






















