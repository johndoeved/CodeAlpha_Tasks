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