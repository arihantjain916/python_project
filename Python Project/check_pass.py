def fetch_user():
    import game_info
    import pandas as pd

    a = input("Enter the username: ").lower()
    b = input("Enter the password: ")

    df1 = pd.DataFrame(pd.read_excel(r"Book1.xlsx"))
    data = df1[['username' , 'password']]
        
    user=[] 
    passw = []   
    for i in range(0,len(data)):
        user.append(data.loc[i][0])
        passw.append(data.loc[i][1])
    for x in range(0,len(user)):
        if((a==user[x]) and (b ==passw[x])):
            print("Entry Granted")
            a = input("You want to play game? ")
            if a == "yes":
                game_info.game()
            else:
                print("")
                
# fetch_user()
