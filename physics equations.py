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

half = .5

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
            print("Please Choose Which Variable You Want To Solve For: ")
            print("1. Initial Velocity")
            print("2. Acceleration")
            print("3. Time")
            print("4. Displacement Of X:")
            whattosolvefor = int(input("Please Type Corresponding Number Here: "))
            notanswered = False
# Matches User Input To What Formula They Want To Use
            match whattosolvefor:                
# Formula For No Final Velocity, deltax = vi * t + .5 * a * t^2
                case 1:
                    accel = float(input("Please Input Value Of Acceleraton Here: "))
                    time = float(input("Please Input Value Of Time Here: "))
                    deltax = float(input("Please Input Value Of Displacement Of X Here:"))
                    finalanswer = (deltax // time) - (half * accel * (time * time))
                    print("Initial Velocity Is Equal To: " , finalanswer)
                    notanswered = False
                case 2:
                    time = float(input("Please Input Value Of Time Here: "))
                    deltax = float(input("Please Input Value Of Displacement Of X Here:"))
                    vi = float(input("Please Input Your Initial Velocity Here: ")) 
                    finalanswer = 2 ((deltax - vi) // time)
                    print("Acceleration Is Equal To: " , finalanswer)
                    notanswered = False
                case 3:
                    accel = float(input("Please Input Value Of Acceleraton Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here: ")) 
                    deltax = float(input("Please Input Value Of Displacement Of X Here:"))
                    finalanswer = ((deltax / (half * accel)) - vi)
                    print("Time Is Equal To: " , finalanswer)
                    notanswered = False
                case 4:
                    time = float(input("Please Input Value Of Time Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here: ")) 
                    accel = float(input("Please Input Value Of Acceleraton Here: "))
                    finalanswer = 2 * ((deltax / (time * time)) - (vi * time))
                    print("Displacement Of X Is Equal To" , finalanswer)
                    notanswered = False
# No Initial Velocity
        case 2:
            print("Please Choose Which Variable You Want To Solve For: ")
            print("1. Final Velocity")
            print("2. Acceleration")
            print("3. Time")
            print("4. Displacement Of X:")
            whattosolvefor = int(input("Please Type Corresponding Number Here: "))

            match whattosolvefor: 

                case 1:
                    accel = float(input("Please Input Value Of Acceleration Here: "))
                    time = float(input("Please Input Value Of Time Here: "))
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    finalanswer = (deltax + (.5(accel * time)))
                    print("Value Of Final Velocity Is Equal To: " , finalanswer)
                    notanswered = False
                case 2:
                    time = float(input("Please Input Value Of Time Here: "))
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    finalanswer = ((deltax / (time * time)) - (vf * t)) * -2
                    print("Value Of Acceleration Is Equal To: " , finalanswer)
                    notanswered = False
                case 3:
                    accel = float(input("Please Input Value Of Acceleration Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    finalanswer = ((deltax - vf) / (-.5 * accel))
                    print("Value Of Time Is Equal To: " , finalanswer)
                    notanswered = False
                case 4:
                    accel = float(input("Please Input Value Of Acceleration Here: "))
                    time = float(input("Please Input Value Of Time Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    finalanswer = (vf * t) - (-.5 * a * (time * time))
                    print("Value Of Displacement Of X Is Equal To: " , finalanswer)
                    notanswered = False
        case 3:
            print("Please Choose Which Variable You Want To Solve For: ")
            print("1. Final Velocity")
            print("2. Initial Velocity")
            print("3. Time")
            print("4. Displacement Of X:")
            whattosolvefor = int(input("Please Type Corresponding Number Here: "))

            match whattosolvefor: 

                case 1:
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    time = float(input("Please Input Value Of Time Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here: "))
                    finalanswer = (2 * ((deltax / time) - (.5 * vi)))
                    print("Value Of Final Velocity Is Equal To: " , finalanswer)
                    notanswered = False
                case 2:
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    time = float(input("Please Input Value Of Time Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    finalanswer = (2 * ((deltax / time) - (.5 * vf)))
                    print("Value Of Initial Velocity Is Equal To: " , finalanswer)
                    notanswered = False
                case 3:
                    deltax = float(input("Please Input Vale Of Displacement Of X Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    finalanswer = (2 * deltax) / (vi + vf)
                    print("Value Of Time Is Equal To: " , finalanswer)
                    notanswered = False
                case 4: 
                    time = float(input("Please Input Value Of Time Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here: "))
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    finalanswer = (.5 * (vf + vi) * t)
                    print("Value Of Displacement Of X Is Equal To: " , finalanswer)
                    notanswered = False

        case 4:
            choice4 == True
            break
        case 5:
            print("Please Choose Which Variable You Want To Solve For:")
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
                    notanswered = False
# Solves For Initial Velocity Without Delta X 

                case 2:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    accel = float(input("Please Input Your Acceleration Here: "))
                    time = float(input("Please Input Your Time Here: "))
                    finalanswer = vf / (accel * time)
                    print("Initial Velocity Is Equal To: ", finalanswer)
                    notanswered = False
# Solves For Acceleration Without Delta X 

                case 3:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    time = float(input("Please Input Time Here: "))
                    vi = float(input("Please Input Initial Velocity Here: "))
                    finalanswer = (vf / time) - vi
                    print(finalanswer)
                    notanswered = False
# Solves For Time Without Delta X 

                case 4:
                    vf = float(input("Please Input Your Final Velocity Here: "))
                    accel = float(input("Please Input Your Acceleration Here: "))
                    vi = float(input("Please Input Your Initial Velocity Here"))
                    finalanswer = (vf / accel) - vi
                    print(finalanswer)
                    notanswered = False
        case _:
            print("Please just input something brother man")
            
    
       



#     vf = input("Please Input Your Final Velocity Here: ")
#    vi = input("Please Input Your Initial Velocity Here")
#    accel = input("Please Input Your Acceleration Here: ")
#    time = input("Please Input Your Of Time Here: ")
#    whattosolvefor = input("What Value Do "

# Problem With User Input 
# if else:

