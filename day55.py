
#snake water gun

import random

# Function to determine the winner
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# Driver code
print("Comp Turn: Snake(s) Water(w) Gun(g)")
randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) Gun(g)? ")
result = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if result is None:
    print("The game is a tie!")
elif result:
    print("You win!")
else:
    print("You lose!")


     
