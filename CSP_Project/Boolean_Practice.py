# Boolean Game (to help future students with understanding boolean equations)

import random

#3 difficulties with different likelyhoods of getting certain inputs
#TODO: expand constant list
T_const1 = ["True", "1==1", "True", "True", "1==1"] #duplicates for difficulty tweak
F_const1 = ["False", "1!=1", "False", "False", "1==1"]
T_const2 = ["True", "1==1", "not(False)", "1==1", "not(False)"]
F_const2 = ["False", "1!=1", "not(True)", "1!=1", "not(True)"]
T_const3 = ["True", "1==1", "not(False)", "bool(0)", "1==1", "not(False)"]
F_const3 = ["False", "1!=1", "not(True)", "bool(1)", "1!=1", "not(True)"]
T_const = [T_const1, T_const2, T_const3]
F_const = [F_const1, F_const2, F_const3]

# defaults
difficulty = 1
rounds = 10 
score = 0

#-----Helper Methods-----
def randbool():
    """return a random boolean"""
    return bool(random.randint(0, 1)) # 0 is false, 1 is true (when cast to boolean in python)

def print_list(list):
    """print a list with spaces between each item"""
    i = 0
    for item in list:
        copy = list.copy()
        try:
            if not((item == "(") or (copy.pop(i+1) == ")")):
                end = " "
            else:
                end = ""
        except:
            if not((item == "(") or (copy.pop(i-1) == ")")): #remove end of list error
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
            if inverse: #flip current boolean if inverted AFTER addition is found
                curr_boolean = not(curr_boolean)
            bool_string.append(addition)
        except: # stop error of not having a current boolean
            curr_boolean = randbool()
            bool_string.append(str(curr_boolean))
        length -= 1

    # ensure bool_string is equal to boolean
    # TODO: FIX THIS!!!!
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
        #and higher priority than or, ensure parentheses before
        if (substring == "and") and (i > 2): #i>2 for parentheses before start
            if not(skip):
                bool_string.insert(0, "(")
                i+=1
                try: #stop end of list error
                    bool_string.insert(i, ")")
                except:
                    print("End of list reached")
                    bool_string.append(")")
                skip = True
                goal = i%2
            elif (i%2 == goal):
                skip = False
        i += 1

    return bool_string

def get_bool_snip(curr_boolean,  inverse = False):
    """if inverse is True, grab a string that will flip the current boolean\n
        otherwise, grab a string that will not flip the current boolean"""
    
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
    else:
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
        r = random.randint(0, len(T_const[difficulty-1]) - 1)
        return T_const[difficulty-1][r]
    elif not(item):
        r = random.randint(0, len(F_const[difficulty-1]) - 1)
        return F_const[difficulty-1][r]

#-----Events----
def start_game():
    """start a new instance of the game"""
    global difficulty, rounds, score
    score = 0
    try:
        rounds = int(input("How many rounds?: "))
        difficulty = int(input("What difficulty would you like to play?(1-3): "))
    except ValueError:
        print("Wrong input, try inputting a number." )
        start_game()
    
    for i in range(0, rounds):
        pscore = score
        boolean = randbool()
        bool_string = create_bool_string(boolean)
        print("What does this result in? ", end="")
        print_list(bool_string)
        answer = input("\nInput(T/F): ")
        if boolean:
            if answer == "T":
                score += difficulty
        else:  
            if answer == "F":
                score += difficulty
        if pscore == score:
            print("Too bad, this one was " + str(boolean))
        else:
            print("Yes! This was " + str(boolean))
        print("Score: "  + str(score))
    
    print("Your final score was: " + str(score/(rounds*difficulty)*100) + "%, for " + str(rounds) + " rounds")
        
    if (input("Would you like to try again?(y/n): " == "y")):
        start_game()



# preface at start
print("To begin answer a few questions about the game by typing in the terminal and pressing enter.")
start_game()


