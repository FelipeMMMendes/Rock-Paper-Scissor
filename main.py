from imprime import imprime
import random
from regras import conditions

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)

ComputerChoice = random.randint(0,2)

imprime(choice)

print("Computer choose: \n")

imprime(ComputerChoice)

conditions(choice,ComputerChoice)
