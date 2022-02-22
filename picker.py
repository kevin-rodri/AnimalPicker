keepGoing = True
while keepGoing == True:
    print("What animal would you like to see: Dog or Cat")
    userInput = input()
    if userInput.lower() == 'dog':
        print("^..^      /\n/_/\\_____/\n   /\\   /\\\n  /  \\ /  \\")
        keepGoing = False
    elif userInput.lower() == 'cat':
        print(" /\\_/\\\n( o o )\n==_Y_==\n  `-\'")
        keepGoing = False
    else:
        print("Invalid option")
