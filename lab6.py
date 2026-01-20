# 1.WAP to demonstrate the indexing and slicing of a list and tuple.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"List: {list1}")
print(f"Tuple: {tuple1}")
print(f"Element at index 3 in list: {list1[3]}")
print(f"Element at index 3 in tuple: {tuple1[3]}")
print(f"Elements from index 3 to 7 in list: {list1[3:8]}")
print(f"Elements from index 3 to 7 in tuple: {tuple1[3:8]}")
print(f"Elements from index 3 to end in list: {list1[3:]}")
print(f"Elements from index 3 to end in tuple: {tuple1[3:]}")
print(f"Elements from start to index 7 in list: {list1[:8]}")
print(f"Elements from start to index 7 in tuple: {tuple1[:8]}")
print(f"Elements from start to end in list: {list1[:]}")
print(f"Elements from start to end in tuple: {tuple1[:]}")

#2.	WAP to iterate an element of list and tuple using for and while loops.
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
print("List elements using for loop:")
for i in list1:
    print(i)
print("Tuple elements using for loop:")
for i in tuple1:
    print(i)
print("List elements using while loop:")
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print("Tuple elements using while loop:")
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1

#3.	WAP that creates a list of 10 random integers. Then create two lists of all odd and even numbers from it.  
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Original list: {list1}")
print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")

#4.	WAP that creates a list of words by combining the words in two individual lists.
# WAP that creates a list of words by combining the words in two individual lists.
list1 = ["hello", "world", "python"]
list2 = ["programming", "is", "fun"]

combined_list = []

for word1 in list1:
    for word2 in list2:
        combined_list.append(word1 + " " + word2)

print("Combined list of words:")
print(combined_list)

#5.	WAP to remove all duplicates from a list.
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(f"Original list: {list1}")
print(f"List after removing duplicates: {unique_list}")

#6.	WAP to combine values in two lists using list comprehension. 
# Combine only those values of a list that are multiples of values in the first list.
list1 = [1, 2, 3, 4, 5]
list2= [10, 20, 30, 40, 50]
combined_list = [i * j for i in list1 for j in list2 if j % i == 0]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Combined list: {combined_list}")

#7.	WAP using filter() function to filter out only even numbers from a list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, list1))
print(f"Original list: {list1}")
print(f"Even numbers: {even_numbers}")

#8.WAP using map() function to create a list of squares of numbers in the range 1 to 10.
squares = list(map(lambda x: x ** 2, range(1, 11)))
print(f"Squares of numbers from 1 to 10: {squares}")

#9.	WAP to demonstrate the use of zip() and enumerate() functions.
list1 = [1, 2, 3, 4, 5]
list2 = ["one", "two", "three", "four", "five"]
print("Enumerate:")
for i, value in enumerate(list1):
    print(f"Index: {i}, Value: {value}")
print("Zip:")
for i, j in zip(list1, list2):
    print(f"List1: {i}, List2: {j}")

#10.WAP to add two matrices (using nested lists).
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matrix 1:")
for row in matrix1:
    print(row)
print("Matrix 2:")
for row in matrix2:
    print(row)
print("Resultant Matrix:")
for row in result:
    print(row)
#11.WAP to return the highest and lowest values in the list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
highest = max(list1)
lowest = min(list1)
print(f"Original list: {list1}")
print(f"Highest value: {highest}")
print(f"Lowest value: {lowest}")













    









