try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("i am always executed")
    ## the use of the finally is that hona hi hai ye statement print
    