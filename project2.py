import random
import time

OPERATORS=["+","-","*"]
min_operand=3
max_operand=12
total_problems=10

def genarete_problem():
  left=random.randint(min_operand,max_operand)
  right=random.randint(min_operand,max_operand)
  operator=random.choice(OPERATORS)

  expr=str(left)+" "+operator+" "+str(right)
  answer=eval(expr)
  return(expr,answer)

wrong=0
print("press enter to start!")
print("--------------------------")

start_time=time.time() #special thing about timer
for i in range(total_problems):
  expr,answer=genarete_problem()
  while True:
    guess=input("problem #"+str(i+1)+": "+expr+ "=")
    if guess==str(answer):
       break
    wrong +=1

end_time = time.time()#special thing about timer
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")

