## 3.WAP to demonstrate exceptions in python considering ZeroDivisionError, ValueError, AttributeError, NameError, ImportError, IOError.  
from nonexistent_module import something

try:
    # ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError occurred: {e}")

try:
    # ValueError
    num = int("abc")
except ValueError as e:
    print(f"ValueError occurred: {e}")

try:
    # AttributeError
    x = 10
    x.append(5)
except AttributeError as e:
    print(f"AttributeError occurred: {e}")

try:
    # NameError
    print(undefined_variable)
except NameError as e:
    print(f"NameError occurred: {e}")

try:
    # ImportError
    from nonexistent_module import something
except ImportError as e:
    print(f"ImportError occurred: {e}")

try:
    # IOError
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"IOError occurred: {e}")
## 4.	WAP that asks the user to input two numbers and following information:
#a.	Try to convert the user inputs to integers and perform division operation (num1 / num2).
#b.	Handle any possible exceptions that may occur during the conversion or division operation.
#c.	Print appropriate error messages for each type of exception (e.g., ValueError, ZeroDivisionError), if it occurs.
#d.	Ensure that the program continues to execute even if an exception occurs.
def divide_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
            break  # Exit the loop if division is successful
        except ValueError as e:
            print(f"ValueError occurred: {e}. Please enter valid integers.")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError occurred: {e}. Cannot divide by zero. Please enter a non-zero second number.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

#5.WAP to demonstrate pickling process without file and with file using pickledump() and pickleload() functions.




