## WAP to remove nth index character from a non-empty string.
str = input("Enter a string: ")
n = int(input("Enter the index of the character to remove: "))
print("Original string:", str)
print("Index to remove:", n)
new_str = str[:n] + str[n+1:]
print("String after removing the character:", new_str)





# for char in input_string:
        length += 1
    return length

# Example usage
test_string = "Hello, World!"
print(f"The length of the string is: {calculate_length(test_string)}")


# WAP to calculate the length of a string Do not use built in function len( ).

def calculate_length(input_string):
    length = 0
    for char in input_string:
        length += 1
    return length

# Example usage
test_string = "Hello, World!"
print(f"The length of the string is: {calculate_length(test_string)}")