primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 71, 73, 79, 83, 89, 97]


#list integer values
def get_integer_list(factor, end):
    list = []
    integer = factor
    while (integer <= end):
        list.append(integer)
        integer += factor
    return list

def go():
    print("This program will list all the integer values that have a certain prime as a factor.")
    y = True
    while (y == True):
        end = int(input("Test integers from 2 to what? "))
        num_of_primes = int(input("How many prime numbers? "))
        for prime in range(num_of_primes):
            print_factors(primes[prime], end)
        
        # ask user about repeat
        if ("y" == input("Would you like to try again?(y/n) ")):
            y = True
        else:
            y = False

def print_factors(prime, end):
    int_list = get_integer_list(prime, end)
    if (int_list == []):
        integer_string = "No values have this as a factor"
    else:
        conditional = (len(int_list) > 1)
        if conditional:
            last_int = int_list.pop()
        integer_string = str(int_list)
        integer_string = integer_string.replace('[', '')
        integer_string = integer_string.replace(']', '')
        if conditional:
            integer_string = integer_string + " and " + str(last_int)

    print("Has " + str(prime) + " as a factor:")
    print("\t" + integer_string)
    print()


go()