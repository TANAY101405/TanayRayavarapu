import random

def game():
  while True: 
    task1 = input("Hi! Welcome to rock paper scissors. Which hand would you like to choose?\n")
  
    computer = random.randint(0,2)
    if computer == 0:
      choice = "rock"
    elif computer == 1:
      choice = "paper"
    else:
      choice = "scissors"
  
  
    print("The computer chose " + choice)
    #All the possibilites if the game ends with a tie
    if task1 == choice:
      print("You tie, go again")
      #This is where the code is going to go
    elif task1 == choice:
      print("You tie, go again")
      #This is where the code is going to go
    elif task1 == choice:
      print("You tie, go again")
  
  
    #All the possibilites where the computer has choosen paper
    if task1 == "rock" and choice =="paper":
      print("The computer wins")
    if task1 == "rock" and choice == "scissors":
      print("You won")
  
  
  
  
    #All the possibilities where you have chosen paper
    if task1 == "paper" and choice == "scissors":
      print("You have lost!")
    elif task1 == "paper" and choice == "rock":
      print("Good job, you have won!")
  
  
    #All the possibilities where you have chosen scissors
    if task1 == "scissors" and choice == "paper":
      print("Good job, you won!")
    elif task1 == "scissors" and choice == "rock":
      print("You have lost!")
    
    keepPlay = input("Would you like to stop or continue! \n")
    if keepPlay == "stop":
      print("Thank you for playing Rock Paper Scissors!")
      break
  
      
    