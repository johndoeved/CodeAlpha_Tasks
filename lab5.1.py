## WAP to print the following pattern:
# A
# A B
# A B C
# A B C D
# A B C D E
N=6
for i in range(1,N):
   ch='A'
   print()
   for j in range(1,i+1):
       print(ch, end=' ')
       ch=chr(ord(ch)+1)

      