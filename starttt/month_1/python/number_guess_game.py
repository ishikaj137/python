import random
number= random.randint(1,100)
while True:
   guess= int(input("guess the number"))
   if(guess>number):
    print("too large, guess again")
   elif(guess<number):
    print("too small, guess again")
   else:
    print("congrats! correct number")
    break