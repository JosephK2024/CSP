# Boolean Game (to help future students with understanding boolean equations)

import random

#TODO: expand constant list
T_const = ["True", "bool(0)", "not(False)"]
F_const = ["False", "bool(1)", "not(True)"]

def randbool():
    """return a random boolean"""
    return bool(random.randint(0, 1)) # 0 is false, 1 is true (when cast to boolean in python)

def create_bool_string(boolean):
    """create a string with 'equal value' to the inputted boolean and return"""
    
    # Create ors/ands and assign groups to T/F
    bool_string = []
    length = random.randint(2, 5) # length of this boolstring
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
    
    print(bool_string)
    
    # give T/F random pre-defined 'constant string'
    for substring in bool_string:
        i = bool_string.index(substring)
        if substring == "True":
            bool_string.pop(i)
            bool_string.insert(i, get_const(True))
        elif substring == "False":
            bool_string.pop(i)
            bool_string.insert(i, get_const(False))

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
    global T_const, F_const
    if item:
        r = random.randint(0, len(T_const) - 1)
        return T_const[r]
    elif not(item):
        r = random.randint(0, len(F_const) - 1)
        return F_const[r]

def print_list(list):
    """print a list with spaces between each item"""
    for item in list:
        print(item, end=" ")
    print()#newline
    

for i in range(30):
    boolean = randbool()
    print(boolean)
    print_list(create_bool_string(boolean))
    print()#newline
