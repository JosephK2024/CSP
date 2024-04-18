# Integration and other calc functions (basically make a calculator)
#   Includes input, function, and output easily
#       User input(what they want to do and what they want to do to it)
#   Struggling to come up with a way to incorporate lists


# TODO: integration, reading inputs, outputs, all the function-types



#-----Toolbox-----
def integrate():#TODO
    print("Nuh uh")
    run()

def solve_for_x():#TODO
    print("No thanks")
    run()

def simplify():#TODO
    print("Nope")
    run()

def end():#TODO
    quit()

toolbox = [integrate, solve_for_x, simplify, end]

#-----Helper Methods-----
def run():
    """runs the program, allowing for repitition"""
    i = 1
    for tool in toolbox:
        print(str(i) + ".", end=" ")
        toolString = func_to_str(tool)
        print(toolString)
        i+=1
    
    UInput = input("Which tool would you like to choose? ")
    for tool in toolbox:
        try:
            if (int(UInput) == toolbox.index(tool) + 1):
                tool()
        except:
            print("Try inputting the number of the tool you want to use\n")
            run()
        

def func_to_str(function):
    strVer = str(function)
    strVer = strVer.split(" ")[1]
    strVer = strVer.capitalize()
    strVer.replace("_", " ")#TODO: fix underscores
    return strVer

        

#Begin program
run()