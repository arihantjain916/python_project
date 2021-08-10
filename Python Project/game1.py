def quiz():

    print('Welcome to Quiz')
    answer=input('Are you ready to play the Quiz ? (yes/no) :')
    score=0
    total_questions=5
    
    if answer.lower()=='yes':
        answer=input('Question 1: What is the lifespan of a dragonfly?')
        if answer.lower()=='24 hours':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')
    
    
        answer=input('Question 2: What moves around the farm without moving? ')
        if answer.lower()=='fence':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')
    
        answer=input('Question 3: Peters father has five sons. The names of four sons are Fefe, Fifi, Fafa and Fufu respectively. What is the name of the fifth son? ')
        if answer.lower()=='peter':
            score += 1
            print('correct')
        else:
            print('Wrong Answer :(')
    
    print("Thankyou for Playing this small quiz game")
    print(f"Your score is {score}")
    print('BYE!')