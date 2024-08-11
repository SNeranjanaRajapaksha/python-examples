import random

user_wins=1
computer_wins=1


options=["paper","scissor","rock"]

random_number=random.randint(0,2) #0,1,2

computer_input=options[random_number]


while True:
 user_input=input("Enter paper,scissor or rock and Q to quit: ").lower() #paper
 print(computer_input)
  
 if user_input=="q":
   break

 elif user_input=="paper" and computer_input=="rock":
        print("you won! you have "+str(user_wins))
        user_wins +=1
 elif user_input=="rock" and computer_input=="scissor":
        print("you won!you have " +str(user_wins))
        user_wins +=1
 elif user_input=="scissor" and computer_input=="paper":
        print("you won! you have " +str(user_wins))
        user_wins +=1
 else:
        print("you lost!Computer have " +str(computer_wins))
        computer_wins+=1

print("your marks: "+str(user_wins))
print("computer marks: "+str(computer_wins))
print("Good byee")
        

