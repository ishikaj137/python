import sys    #input at run promt
if len(sys.argv)<2:    #2 for prompt and input
    print("too few args")
elif len(sys.argv>2):
    print("too many args")
else:
    print("hello, my name is", sys.argv[1])