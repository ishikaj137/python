name=input("what's your name")
match name:
    case "Ishika":
        print("good girl")
    case "avika":
        print("good grl")
    case "muma":
        print("good woman")
    case "papa":
        print("good man")
    

    #or

    case "Ishika"|"avika"|"muma"|"papa":
        print("good person")
    case _: #whoever or whatever
        print("idk you")