## WAP to iterate a given string using while and for loop.
str = input("Enter a string: ")
print("Original string:", str)
print("Using for loop:")
for i in str:
    print(i)
print("Using while loop:")
i=0
while i<len(str):
    print(str[i])
    i+=1
