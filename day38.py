## raising custom error
a = int(input("enter any value between 5 and 9 is: "))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9 is: ")
