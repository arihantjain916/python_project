def game():
    while True:
        # import emoji
        import game1
        import game2
        import game3
        import game4

        print("Welcome to the world of game")
        print("There are total 4 games")
        print("Here are the list of game available here")
        print("""1. Quiz game
        2. Guessing the number
        3. Snake water Gun
        4. Stone Paper Scissor
        """)
        a = int(input("Enter the code of the game you want to play: "))
        if a == 1:
            game1.quiz()
        elif a == 2:
            game2.guess()
        elif a == 3:
            game3.swg()
        elif a == 4:
            game4.sps()
        else:
            print("invalid choice.")
        a = input("You want to play more(yes/no): ").lower()
        if a == "yes":
            continue
        else:
            print("Thank you for playing... \U0001f600 ")
            break

# game()
