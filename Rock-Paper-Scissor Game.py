import random
computer_score,user_score=0,0
while True:
    option=['stone','paper','scissor']
    a=random.choice(option)
    user_input=input('''enter ur option 1.stone
    2.paper
    3.scissor
    press q to exit
    enter ur value:''')
    if user_input.isdigit()==True:
        user_input=int(user_input)
        if option[user_input-1]==a:
            print("Both Computer and User have same symbol")
            computer_score,user_score=computer_score,user_score
        elif option[user_input-1]=='stone':
            if a=='paper':
                computer_score+=1
                print("computer wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
            elif a=='scissor':
                user_score+=1
                print("user wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
        elif option[user_input-1]=='paper':
            if a=='scissor':
                computer_score+=1
                print("computer wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
            elif a=='stone':
                user_score+=1
                print("user wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
        elif option[user_input-1]=='scissor':
            if a=='stone':
                computer_score+=1
                print("computer wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
            elif a=='paper':
                user_score+=1
                print("user wins")
                print("computer score:",computer_score," user score:",user_score)
                print("")
    elif user_input.isdigit()==False:
            if str(user_input)=='q':
                print("final score")
                print(" ")
                print("computer score=",computer_score,"user score=",user_score)
                break
            else:
                print("invalid input")
                
