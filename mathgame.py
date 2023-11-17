import mypythonfunction

userName=input("give us your name pls \n")

UserChoice='0'
while UserChoice=='0':
    userScore=(mypythonfunction.getuserpoint(userName)) #check if new user or not
    if userScore=='-1':
        newUser=True
        userScore='0'
    else:
        newUser=False

    if UserChoice!='-1':
        mypythonfunction.question(userName,newUser)
    
        UserChoice=input("write -1 to stop playing or WRITE 0 to keep playing \n")
    else :
        break