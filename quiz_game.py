Count=0
print("Welcome to my quiz game")

Playing = input("Do you want to play quiz game ")
if Playing.lower()!="yes":
    quit()

print("okay!Let's play:)-")

answer=input("What is the stand for CPU: ")
if answer.lower()=="central processing unit":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")
       
answer=input("What is the stand for GPU: ")
if answer.lower()=="graphical processing unit":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")

answer=input("What is the stand for RAM: ")
if answer.lower()=="random access memory":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")

answer=input("What is the stand for ROM: ")
if answer.lower()=="read only memory":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")

answer=input("What is the stand for CD: ")
if answer.lower()=="compact disk":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")

answer=input("What is the stand for SUSL: ")
if answer.lower()=="sabaragamuwa univercity of sri lanka":
       print("correct!")
       Count=Count+1
else:
       print("Incorrect")

print("Your score is:",Count)