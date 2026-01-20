# WAP to calculate the length of a string Do not use built in function len( ).
n= input("Enter a string: ")
length = 0
for char in n:
    length += 1
print(f"The length of the string is: {length}")

# 	WAP to return a string in title case. Do not use built in function title( ). (If string is “The world is beautiful”,
#   program should return the string in title case as “The World Is Beautiful”.)
n= input("Enter a string: ")
title_case = ""
for i in range(len(n)):
    if i == 0:
        title_case += n[i].upper()
    elif n[i-1] == " ":
        title_case += n[i].upper()
    else:
        title_case += n[i]
print(f"The string in title case is: {title_case}")

#	WAP to check whether a string is a palindrome or not.
n= input("Enter a string: ")
if n == n[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 7.	WAP to demonstrate the use of various built-in functions such as 
# count, find, isalnum, isalpha, isdigit, islower, isupper, upper, lower,
#  strip, replace, swapcase, join etc.
n= input("Enter a string: ")

print(f"Number of 'a' in the string: {n.count('a')}")
print(f"Index of 'a' in the string: {n.find('a')}")
print(f"Is the string alphanumeric? {n.isalnum()}")
print(f"Is the string alphabetic? {n.isalpha()}")
print(f"Is the string a digit? {n.isdigit()}")
print(f"Is the string in lowercase? {n.islower()}")
print(f"Is the string in uppercase? {n.isupper()}")
print(f"String in uppercase: {n.upper()}")
print(f"String in lowercase: {n.lower()}")
print(f"String after stripping: {n.strip()}")
print(f"String after replacing 'a' with 'b': {n.replace('a', 'b')}")
print(f"String after swapping case: {n.swapcase()}")
print(" ".join([n,"university"]))

#1.	WAP that accepts a string from user and redisplays the same string after removing vowels from it.
n= input("Enter a string: ")
vowels = "aeiouAEIOU"
new_str = ""
for char in n:
    if char not in vowels:
        new_str += char
print(f"String after removing vowels: {new_str}")

#2.	WAP to find whether a given character is present in a string or not. In case it is present,
#  print the index at which it is present. Do not use built-in find function to search the character.
n= input("Enter a string: ")
char = input("Enter a character to search: ")
index = 0
for i in range(len(n)):
    if n[i] == char:
        index
        print(f"The character '{char}' is present at index {i}.")
        break
if index == -1:
    print(f"The character '{char}' is not present in the string.")


# 3.	WAP to count the occurrence of each word in a given sentence.
n= input("Enter a sentence: ")
words = n.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word count in the sentence:")
for key, value in word_count.items():
    print(f"{key}: {value}")
    
    #5.	Write a function to convert a given string to all uppercase if it contains at 
    # least 2 uppercase characters in the first 4 characters.
    n= input("Enter a string: ")
count = 0
for i in range(4):
    if n[i].isupper():
        count += 1
if count >= 2:
    print(f"String in uppercase: {n.upper()}")
else:
    print(f"String does not contain at least 2 uppercase characters in the first 4 characters.")

    #6.	WAP to remove existing indentation from all the lines in a given text.
    n= int(input("Enter the number of lines: "))
lines = []
for i in range(n):
    lines.append(input(f"Enter line {i+1}: "))
print("Original text:")
for line in lines:
    print(line)
print("Text after removing indentation:")
for line in lines:
    print(line.lstrip())

    


