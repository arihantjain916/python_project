def sps():
    import random

    # Stone paper Scissor
    def gameWin(comp, you):
    
        if comp == you:
            return 8
    # win = true
    # harna = false
        elif comp == 's':
            if you=='g':
                return False
            elif you=='p':
                return True
        
        elif comp == 'p':
            if you=='s':
                return False
            elif you=='g':
                return True

        elif comp == 'g':
            if you=='p':
                return False
            elif you=='s':
                return True

    print("Comp Turn: Stone(s) Paper(p) or Scissor(g)?")
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 'g'

    you = input("Your Turn: Stone(s) Paper(p) or Scissor(g)?")
    a = gameWin(comp, you)

    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    if a == 8:
        print(f"Computer chose {comp}")
        print(f"You chose {you}")
        print("The game is a tie!")
    elif a == True:
        print(f"Computer chose {comp}")
        print(f"You chose {you}")
        print("You Win!")
    elif a == False:
        print(f"Computer chose {comp}")
        print(f"You chose {you}")
        print("You Lose!")
    else:
        print('You choose wrong input')
    