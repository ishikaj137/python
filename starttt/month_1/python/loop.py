#while loop
i=0
while i<3:
    print("hello")
    i=i+1

#for loop
for i in range(5): #or for _ in range(5):
    print("hello1")

#or
print("hello2\n"*5)

#taking iteration input
while True:
        n=int(input("how many times?"))
        if n>0:
            break

for _ in range(n):
    print("hello3")

#function
def main():
    n=get_num()
    meow(n)
def get_num():
    while True:
        n=int(input("whats n?"))
        if n>0:
          return n
def meow(n):
    for _ in range(n):
        print("hello4")

     
main()