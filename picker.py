keepGoing = True
while keepGoing == True:
    print("What animal would you like to see: Dog, Cat, or Fish")
    userInput = input()
    if userInput.lower() == 'dog':
        print("^..^      /\n/_/\\_____/\n   /\\   /\\\n  /  \\ /  \\")
        keepGoing = False
    elif userInput.lower() == 'cat':
        print(" /\\_/\\\n( o o )\n==_Y_==\n  `-\'")
        keepGoing = False
    elif userInput.lower() == 'fish':
        print("      o                 o\n                  o\n         o   ______      o\n           _/  (   \\_\n _       _/  (       \\_  O\n| \\_   _/  (   (    0  \\\n|== \\_/  (   (          |\n|=== _ (   (   (        |\n|==_/ \\_ (   (          |\n|_/     \\_ (   (    \\__/\n          \\_ (      _/\n            |  |___/\n           /__/")
        keepGoing = False
    else:
        print("Invalid option")
