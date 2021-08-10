import generatepass as gp
import check_pass as cp
c = input("You are new user or old user: ").lower()
if c == "old":
    cp.fetch_user()
elif c == "new":
    gp.genpass()
else:
    print("Thank you")