#random

import random  #random library 
coin= random.choice(["heads","tails"])
print(coin)
#or
from random import choice
coin= choice(["heads","tails"])
print(coin)


#randint

import random
number=random.randint(1,10)
print(number)


#random.shuffle(x)

import random
cards=["king","queen","jack"]
random.shuffle(cards)
for i in cards:
    print(i)