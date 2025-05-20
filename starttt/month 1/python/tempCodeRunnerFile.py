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