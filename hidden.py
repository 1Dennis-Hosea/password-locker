import getpass

def requestPassword():
    correctPassword ="dennis"
    key = getpass.getpass() #input("Enter password: ")
   

    if key == correctPassword:
         return True
    return False

if requestPassword():
        print('Welcome here')
        x = 74656
        print(x)