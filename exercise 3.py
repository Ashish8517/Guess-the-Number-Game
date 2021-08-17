a = 23
b = 9
while (True):
    c = int(input("Guess the number:\n"))
    if c <23:
        print("your number is small then the real number")
        b = b - 1
        print("you have only", b ,"Guesses left")
        if b==0:
            print("Game Over")
            break
        d = int(input("Press 1 if you try again:\n"))
        if d == 1:
            continue
        else:
            print("you press wrong button")
            break
    elif c>23:
        print("Your number is bigger then the real number")
        b = b - 1
        print("you have only" , b , "Guesses left")
        if b==0:
            print("Game Over")
            break
        e = int(input("Press 1 if you try again:\n"))
        if e == 1:
            continue
        else:
            print("you press wrong button")
            break
    elif c==23:
        print("hurrry you sucessfully guess the number")
        break