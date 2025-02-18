# Dice Roller
# By Anna Vahtera 2020
#
# accepts "x" or "ndx" as argument [ex: 2d6]
# Where n is the number of dice to roll and x is the faces of the die. 
# if n is omitted, it defaults to 1.
# if "7" is chosen [Either argument '7' or 'd7'],
# Roller subsitutes a special case for The Seven RPG. 
# You can add "s" as another argument after the first one to see the intermediate rolls and not just total.

import sys
import random

arguments = len(sys.argv) - 1
result = 0
theseven = 0
random.seed()
combi = ""
sevenresult = ""
number = 1
r = 0
wd = 0
wodTN = 0 
arg1 = ""
sucs = 0
fails = 0
showRolls = False

def errorHandler():
    print()
    print("Allowed arguments are: [n]dx, where x is the type n is the amount of dice to roll. n can be omitted and defaults to 1.")
    print("If '7' or 'd7' is used, the system will subsitute The Seven RPG system dicerolls instead of regular dice.")
    print("You can also use 'w' instead of 'd' between the two numbers to switch to Storyteller Dice (number of d10 against Target Number)")
    print("You can add 's' as another argument after the first one to see the intermediate rolls and not just the total.")
    sys.exit()

if (arguments < 1):
    errorHandler()

if (sys.argv[1].isnumeric()):
    die = int(sys.argv[1])
else:
    r = sys.argv[1].find("d")
    wd = sys.argv[1].find("w")
    arg1 = sys.argv[1]
    if (r > 0):
        if arg1[r + 1:].isnumeric():
            die = int(arg1[r + 1:])
    elif (wd > 0):
        if arg1[wd + 1:].isnumeric():
            die = int(arg1[wd + 1:])

    else:
        errorHandler()

wodTN = die


if (die < 2):
    print()
    print("You cannot have a die with less than two faces. It's impossible.")
    print()
    sys.exit()
    
if (r == 0):
    number = 1
else:
    if (r > 0):
        number = int(arg1[0:r])
    else:
        number = int(arg1[0:wd])
        die = 10
   
for u in range(number):
    r = random.randint(1, die)
    result = result + r
    if (r >= wodTN):
        sucs =  sucs  + 1
    elif (r == 1):
        fails = fails  + 1
    combi = combi + " " + str(r) + " "
print()


for u in range(len(sys.argv)):
    if (sys.argv[u] == "s"):
        showRolls = True

if (wd > 0):
    if bool(showRolls):
        print("Rolling " + str(number) + " against TN" + str(wodTN) + ": [" + combi + "]")
    else:
        print("Rolling against TN" + str(wodTN) + ":")
    if (sucs > fails):
        if ((sucs - fails) == 1):
            print("Result: Marginal Success (" + str(sucs - fails) + ")")
        elif ((sucs - fails) == 2):
            print("Result: Partial Success (" + str(sucs - fails) + ")")
        elif (2 < (sucs - fails) < 5):
            print("Result: Success (" + str(sucs - fails) + ")")
        elif ((sucs - fails) >= 5):
            print("Result: Critical Success (" + str(sucs - fails) + ")")
        
    elif (sucs == fails):
        print("Result: Failure. (" + str(sucs) + " Successes, " + str(fails) + " Failures)")
    else:
        print("Result: Botch. (" + str(sucs) + " Successes, " + str(fails) + " Failures)")
    print()
    print()
    sys.exit()

if (die != 7):
    if bool(showRolls):
        combi = " [" + combi + "]: "
    else:
        combi = ": "
        
    print("Rolling " + str(number) + "d" + str(die) + combi + str(result))
else:
    for u in range(number):
        combi = ""
        theseven = 0
        for u in range(4):
            result = random.randint(1,6)
            if (result == 6):
                theseven = theseven + 1
                combi = combi + " +1 "
            elif (result == 1):
                theseven = theseven - 1
                combi = combi + " -1 "
            else:
                combi = combi + "  0 "
                
        if (theseven > 0):
            sevenresult = "+" + str(theseven)
        else:
            sevenresult = '{:>2}'.format(str(theseven))        
        if bool(showRolls):
            combi = "[" + combi + "]: "
        else:
            combi = ": "
            
        print("Rolling dice for The Seven " + combi + sevenresult)

print()
print()