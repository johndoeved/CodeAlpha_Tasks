a=330000
b=3303
print("A")if a>b else print("=")if a==b else print("C")

c=9 if a>b else 0
print(c)
# Demonstrating indexing and slicing of a string

# Define a sample string
sample_string = "Hello, World!"

# Indexing
print("Original string:", sample_string)
print("Character at index 0:", sample_string[0])  # First character
print("Character at index 7:", sample_string[7])  # Eighth character
print("Character at index -1:", sample_string[-1])  # Last character

# Slicing
print("Substring from index 0 to 4:", sample_string[0:5])  # First five characters
print("Substring from index 7 to end:", sample_string[7:])  # From eighth character to end
print("Substring from start to index 4:", sample_string[:5])  # First five characters
print("Substring with step 2:", sample_string[::2])  # Every second character
print("Reversed string:", sample_string[::-1])  # Reversed string


# Program to print the specified pattern

# Number of rows
n = 5

# Loop through each row
for i in range(n):
    # Loop through each column in the row
    for j in range(i + 1):
        # Print the character corresponding to the ASCII value of 'A' + j
        print(chr(65 + j), end=" ")
    # Move to the next line after each row
    print()