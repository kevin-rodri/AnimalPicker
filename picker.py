keepGoing = True
while keepGoing == True:
    print("What animal would you like to see: Dog or Cat")
    userInput = input()
    if userInput.lower() == 'dog':
        print("Dog ASCII ART HERE")
        keepGoing = False
    elif userInput.lower() == 'cat':
        print("Cat ASCII ART HERE")
        keepGoing = False
    else:
        print("Invalid option")
