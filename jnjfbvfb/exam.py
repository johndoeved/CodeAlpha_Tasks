## Write a program for the list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [x + y for x in list1 for y in list2]
print(list3)

rows = 5 
for i in range(rows): 
 print(" " * i + "*" * (2 * (rows - i) - 1))

 rows =10
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1)) 


# Program to print a pyramid pattern of numbers
    rows = 5 
for i in range(1, rows + 1): 
    # Print leading spaces to center the numbers 
    print(" " * (rows - i), end="") 
 
    # Print numbers from 1 to (2*i - 1) 
    for j in range(1, 2 * i): 
        print(j, end="") 
 
    print()  # Move to the next line