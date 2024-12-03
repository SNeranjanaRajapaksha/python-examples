import random
top_of_range=input("Enter the top of range for expect you guessing range: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Enter the positive number next time.")
        quit()
    else:
        guess_number=input("Enter a guess number:")
        guess_number=int(guess_number)


randm_number=random.randint(0,top_of_range)

guess_count=1
while True:
    if guess_number==randm_number:
        print("you got it in " +str(guess_count)+" times")
        break
    elif guess_number> randm_number:
        print("random number above guess number")
    else:
        print("random number top guess number")
    guess_count+=1
    guess_number=input("Enter a guess number:")
    guess_number=int(guess_number)