# 1-D Kinematics Physics Equations Solver


# Defines All Variables Used In Program Before Usage
vf = float
vi = float
accel = float
time = float
deltax = float 
equationtype = int
choice1 = bool
choice2 = bool
choice3 = bool
choice4 = bool
choice5 = bool
notanswered = True
whattosolvefor = int
finalanswer = int

# Begins Loop For Choosing Which Formula To Use 

while notanswered == True:
    print("1-D Kinematics Problem Solver, Made By KDB")
    print("Please Choose Which Variable You Lack Via Entering The Corresponding Number")
    print("1. Final Velocity")
    print("2. Initial Velocity")
    print("3. Acceleration")
    print("4. Time")
    print("5. Displacement Of X")
    equationtype = int(input("Type Here: "))
    
# Uses input from user to choose which equation type, and reruns beginning message if user inputs invalid input

    match equationtype:
        case 1:
            choice1 == True
            break
        case 2:
            choice2 == True
            break
        case 3:
            choice3 == True
            break
        case 4:
            choice4 == True
            break
        case 5:
            print("Please Choose Which Value You Want To Solve For:")
            print("1. Final Velocity")
            print("2. Initial Velocity")
            print("3. Acceleration")
            print("4. Time")
            whattosolvefor = int(input("Please Type Corresponding Number Here:"))
# Matches What Variable They Are Missing, To The Formula To Solve For Said Variable.

            match whattosolvefor:

# Solves For Final Velocity Without Delta X 
                case 1:
                    vi = float(input("Please Input Your Initial Velocity Here: "))
                    accel = float(input("Please Input Your Acceleration Here: "))
                    time = float(input("Please Input Time Here: "))
                    finalanswer = vi + (accel * time)
                    print("Final Velocity Is Equal To: " , finalanswer)

# Solves For Initial Velocity Without Delta X 

                case 2:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    accel = float(input("Please Input Your Acceleration Here: "))
                    time = float(input("Please Input Your Time Here: "))
                    finalanswer = vf / (accel * time)
                    print("Initial Velocity Is Equal To: ", finalanswer)

# Solves For Acceleration Without Delta X 

                case 3:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    time = float(input("Please Input Time Here: "))
                    vi = float(input("Please Input Initial Velocity Here: "))
                    finalanswer = (vf / time) - vi
                    print(finalanswer)

# Solves For Time Without Delta X 

                case 4:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    accel = float(input("Please Input Your Acceleration Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here"))
                    finalanswer = (vf / accel) - vi
                    print(finalanswer)

        case _:
            print("Please just input something brother man")
            
    
       



#     vf = input("Please Input Your Final Velocity Here: ")
#    vi = input("Please Input Your Initial Velocity Here")
#    accel = input("Please Input Your Acceleration Here: ")
#    time = input("Please Input Your Of Time Here: ")
#    whattosolvefor = input("What Value Do "

# Problem With User Input 
# if else:

