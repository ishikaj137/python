name=input("what's your name?")
file=open("names.txt", "a") #file=variable name, open=open a file in py,write in file, "w" for write, "a" for append ,close= save the file, r= read
file.write(f"{name}\n")
file.close()