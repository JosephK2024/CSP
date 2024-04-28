# Boolean_Practice.py
# Description: Automatically generates "boolean strings" based
#              on the input of a user and test their knowledge of
#              Booleans and operators often used with Booleans
# Coder(s): Joseph Kennedy
# Date of Completion: April 28, 2024

#The only NON-STUDENT portion of this program (other than built in python)
import random 

#3 difficulties with different likelyhoods of getting certain inputs,
# duplicates for differing difficulty
#TODO: expand constant list
T_const1 = ["True", "(1 == 1)", "(1 != 0)" "True",
             "(1 == 1)", "True", "(1 == 1)", "True"]
F_const1 = ["False", "(1 != 1)", "False", "(1 == 0)",
             "False", "(1 == 0)"]
T_const2 = ["True", "(1 == 1)", "not(False)",
             "(1 == 1)", "not(False)"]
F_const2 = ["False", "(1 != 1)", "not(True)",
             "(1 != 1)", "not(True)"]
T_const3 = ["True", "(1 == 1)", "not(False)", "bool(0)",
             "(1 == 1)", "not(False)"]
F_const3 = ["False", "(1 != 1)", "not(True)", "bool(1)",
             "(1 != 1)", "not(True)"]
T_const = [T_const1, T_const2, T_const3]
F_const = [F_const1, F_const2, F_const3]

# defaults
difficulty = 1
rounds = 10 
score = 0

#-----Helper Methods-----
def randbool():
    """return a random boolean"""
    # 0 is false, 1 is true (when cast to boolean in python)
    return bool(random.randint(0, 1))

def print_list(list):
    """print a list with spaces between each item"""
    i = 0
    for item in list:
        copy = list.copy()
        """there is definitely some errors with the parentheses system
            but it is too bothersome to fix right now"""
        #TODO: fix the error here
        try:
            if not((item == "(") or (copy.pop(i+1) == ")")):
                end = " "
            else:
                end = ""
        except:#end of list error likely
            if not((item == "(") or (copy.pop(i-1) == ")")): 
                end = " "
            else:
                end = ""
        print(item, end=end)
        i += 1
    print()#newline   

#------Boolean Methods-----
def create_bool_string(boolean):
    """create a string with 'equal value' to the inputted boolean and return"""
    global difficulty

    bool_string = [] # main item to be added to
    length = random.randint(1, 3*difficulty) # length of this boolstring

    # Create ors/ands and assign groups to T/F
    while (length > 0):
        try:
            if(curr_boolean):
                print(end="")
            inverse = randbool()
            addition = get_bool_snip(curr_boolean, inverse)
            if inverse:#flip current boolean AFTER addition is found
                curr_boolean = not(curr_boolean)
            bool_string.append(addition)
        except: # stop error of not having a current boolean
            curr_boolean = randbool()
            bool_string.append(str(curr_boolean))
        length -= 1

    # ensure bool_string is equal to boolean
    if (boolean != curr_boolean):
        bool_string.append(get_bool_snip(curr_boolean, inverse=True))
    
    # split or/and from T/F
    for substring in bool_string:
        if len(substring)>5: #if less than 5 then it's alone
            if (substring.find(" ")>=0):
                pstrings = substring.rsplit(" ")
                i = bool_string.index(substring)
                bool_string.remove(substring)
                for string in pstrings:
                    bool_string.insert(i-1, string)
    
    # give T/F random pre-defined 'constant string'
    for substring in bool_string:
        i = bool_string.index(substring)
        if substring == "True":
            bool_string.pop(i)
            bool_string.insert(i, get_const(True))
        elif substring == "False":
            bool_string.pop(i)
            bool_string.insert(i, get_const(False))

    # ensure bool string is equal to boolean (again) using parentheses
    i = 0
    skip = False # account for infinite loop 
    for substring in bool_string: 
        #"and" higher priority than "or", ensure parentheses seperating these
        if (substring == "and") and (i > 2): #i>2 for parentheses before start
            if not(skip):
                bool_string.insert(0, "(") #the start is the best spot for this
                i+=1
                bool_string.insert(i, ")")
                skip = True
                goal = i%2
            elif (i%2 == goal):
                skip = False
        i += 1

    return bool_string

def get_bool_snip(curr_boolean,  inverse = False):
    """if inverse is True, grabs a string that will flip the current boolean\n
        otherwise, grabs a string that will not flip the current boolean"""
    
    concat = "" # begin with empty string
    
    if curr_boolean:
        if(inverse):
            concat = "and False" # only way to invert a True
        else:
            op_dep = randbool()
            if op_dep:
                concat = "and True"
            else:
                concat = "or " + str(randbool())
    else:#!curr_boolean
        if inverse:
            concat = "or True" # only way to invert a False
        else:
            op_dep = randbool()
            if op_dep:
                concat = "and " + str(randbool())
            else:
                concat = "or False"

    return concat

def get_const(item):
    """get a constant equal to the item from a pre-defined list"""
    global T_const, F_const, difficulty
    if item:
        #randomize & return
        r = random.randint(0, len(T_const[difficulty-1]) - 1)
        return T_const[difficulty-1][r]
    elif not(item):
        #randomize & return
        r = random.randint(0, len(F_const[difficulty-1]) - 1)
        return F_const[difficulty-1][r]

#-----Events----
def run_game():
    """start a new instance of the game"""
    global difficulty, rounds, score
    score = 0
    try:
        rounds = int(input("How many rounds?: "))
        #ensure rounds != 0
        if rounds <= 0:
            print("Don't use zero or negitives as the number of rounds.")
            print("-"*50)#formats output
            run_game()
        
        difficulty = int(input("What difficulty would you"+ 
                               " like to play?(1-3): "))
        if (difficulty >= (len(T_const) + 1)) or (difficulty <= 0):
            print("Choose a valid difficulty.")
            print("-"*50)#formats output
            run_game()
        print("-"*50)#formats output
    except ValueError:
        print("Wrong input, try inputting a number." )
        print("-"*50)#formats output
        run_game()
    
    for i in range(0, rounds):
        pscore = score
        boolean = randbool()
        bool_string = create_bool_string(boolean)
        print("What does this result in? ", end="")
        print_list(bool_string)
        answer = input("\nInput(T/F): ")
        answer = answer.upper()
        if boolean:
            if answer[0] == "T":
                score += difficulty
        else:  
            if answer[0] == "F":
                score += difficulty
        if pscore == score:
            print("Too bad, this one was " + str(boolean))
        else:
            print("Yes! This was " + str(boolean))
        print("Score: "  + str(score))
        print("-"*50)#formats output
    
    print("Your final score was: " + str(score/(rounds*difficulty)*100) +
           "%, for " + str(rounds) + " rounds")
    print("-"*50)#formats output
    again = input("Would you like to try again?(y/n): ").lower() 
    if (again== "y"):
        run_game()



# preface at start
print("-"*50)#formats output
print("To begin answer a few questions about the game" +
      " by typing in the terminal"+
       " and pressing enter.")
run_game()
