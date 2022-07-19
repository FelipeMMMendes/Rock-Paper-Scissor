def conditions(p1, p2):
#-----------ROCK----------------  
  if(p1 == 0 and p2 == 2):
    print("You win!")
  if(p1 == 0 and p2 == 1):
    print("You lose!")
  if(p1 == 0 and p2 == 0):
    print("Withdraw!")  
#-----------PAPER---------------    
  if(p1 == 1 and p2 == 0):
    print("You win!")
  if(p1 == 1 and p2 == 2):
    print("You lose!")
  if(p1 == 1 and p2 == 1):
    print("Withdraw!")   
#-----------SCISSORS------------    
  if(p1 == 2 and p2 == 1):
    print("You win!")
  if(p1 == 2 and p2 == 0):
    print("You lose!")
  if(p1 == 2 and p2 == 2):
    print("Withdraw!")   

  elif(p1>2 or p1<0):
    print("Invalid number, you lose!")