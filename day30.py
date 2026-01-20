## recursion
def factorial(n):
  n=int(input("enteer the value of n"))
  
  if(n==0 or n==1):
    return 1
  else:
    return n * factorial(n-1)
  print(n * factorial(n-1))
  
    