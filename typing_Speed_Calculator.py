# In this we need time module
from time import *
import random as r

# for calculation of mistakes
def mistake(para,usertest):
    error=0
    for i in range(len(para)):
        try:
            if para[i]!=usertest[i]:
                error+=1
        except :
            error+=1
    return error


# for calculation of time
def time_calculate(time_start,time_end,user_input):
    time_delay=time_end - time_start
    time_round_off=round(time_delay,2)
    speed=len(user_input)/time_round_off
    return round(speed)




while True:
    choice=int(input('Enter your choice 1.play  2.exit'))
    
    if choice == 1:
        # string which user type
        test=["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.","Hii my name is Gorish Verma","I will be your math teacher from today and for this session."]


        test1=r.choice(test)
        print("***** Typing Speed Calculator *****")
        print(test1)
        print()
        print()


        time1=time() # time started
        testinput=input("Enter: ")
        time2=time() # time ended

        print("Speed: ",time_calculate(time1,time2,testinput))
        print("Error: ",mistake(test1,testinput))
    
    elif choice==2:
        print("Thank You")
        break
    else:
        print("Invalid choice")
