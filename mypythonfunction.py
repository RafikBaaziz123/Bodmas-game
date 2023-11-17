import os
import random



def getuserpoint(nom):

    f = open("score.txt", "r") 
    l=f.readlines()
    f.close()

    for i in range(len(l)): 
        l[i]=l[i].strip()
        l[i]=l[i].split(",")

    for name,score in l:
      if name==nom:
        return score
        
    else:
        return "-1"

def updateuserpoint(newuser,username,score):
   
    x=-1
    f = open("score.txt", "r") 
    l=f.readlines()
    f.close()

    for i in range(len(l)): #l = [['A', '101'], ['B', '102'], ['C', '214'], ['D', '129']]
        l[i]=l[i].strip()
        l[i]=l[i].split(",")
    if newuser:#no need to tmp

        
        f =open("score.txt","a") #use 'a' to append NEW USER
        f.write("\n"+username+','+str(score+1)) #NEWUSER
        f.close()
    else:
        f = open("score.txt", "r") 
        temp =open("userscore.tmp","a")
        for line in f:
            x+=1
            if l[x][0]==username: #if this is the user to be updated
                if x+1==len(l): # if this is not the last user in the file 
                    temp.write(username+','+str(score))#UPDATE 
                else:
                    temp.write(username+','+str(score)+'\n')#to verifie last value dont give newline
            else:

                temp.write(line)#DO NOTHINK
                
        temp.close()
        f.close()
        os.remove('score.txt')
        os.rename("userscore.tmp","score.txt")


def question(nom,newUser):
    operandlist=[0]  
    operatorlist=[""]
    operatordict={1:'+',2:'-',3:'*',4:'**'}

  #tache4.1
    operandlist = random.sample(range(0, 10), 5) #generate liste of random diffrent values 
  #tache4.2   WE SHOULD NOT HAVE  ** twice
    x=4
    for i in range(4): # loop to create the equation 
        val=random.randint(1, x) #choose which operator from operatordict
        operatorlist.append (operatordict[val] )
        if operatordict[val]=="**":#we use x=3 to not have the (**) twice
            x=3  
# tache4.3
    
    questionString=""
    for i in range(len(operandlist)):
        questionString+=operatorlist[i]+str(operandlist[i]) # this is our equation
# tache4.4
    questionString=questionString.replace("**","^")

    print("here is the question  "+questionString)
    result=eval(questionString) # calculate the answer
    print("here is the result  "+str(result))
#tache 4.5

    
    while True:
        x=input("write your answer \n")
        if x.isalpha():
            h=input("please entre number please \n if you want to quit press 0 \n or press enter to contunuies \n")
            if h=='0':
                exit()
        else:
            answer=int(x)
            break
        

    while True:      
        try:
            if answer==result:
                print("your answer is correct good job\n")
                pts=int(getuserpoint(nom))
                updateuserpoint(newUser,nom,pts+1)
                pts=int(getuserpoint(nom))


                
                print("KEEP GOING your score now is  "+str(pts))
                break
            
            else:
                print("sorry wrong answer next time nchlh \n")
                print("here is the correct one   "+str(result))
                break
        except ValueError or TypeError:
            print("please the answer is only a number ")
            break
