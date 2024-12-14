import random

user_score=0
computer_score=0


user_wish=input("Do you want play a PIG game?(yes/no)".lower())
if user_wish=="no":
    quit()
elif user_wish=="yes":
    while True:
        user_random=random.randint(1,6)
        user_random=int(user_random)

        
        print("your luck number is:",user_random)
        if user_random==1:
            print("Now play the computer! your score is:",user_score)
            computer_random=random.randint(1,6)
            computer_random=int(computer_random)
            print("computer luck number is:",computer_random)
            
            if computer_random==1:
                print("Now your turn!computer score is:",computer_score)
                
            else:
                computer_score=computer_score+computer_random
                print(computer_score)
                if computer_score>=100:
                    print("computer win!" )
                    break
                else:
                    pass
        else:
            user_score=user_score+user_random
            print(user_score)
            if user_score>=100:
                print("you win!")
                break
    
else:
    print("invalid input")
    
