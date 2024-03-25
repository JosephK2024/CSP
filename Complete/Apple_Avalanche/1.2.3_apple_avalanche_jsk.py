#-----imports-----
import turtle as trtl
from random import randint


#-----setup-----
# how many fruits will be on the tree
number_of_fruit = 5

# homerow keys (the letters that are currently supported by the functions)
availible_letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
# two global lists for all fruits with their respecitve letter
letters = []
fruits = []

# store the file names of the images
apple_image = "apple.gif" 
pear_image = "pear.gif"

# setup window
wn = trtl.Screen()
wn.setup(width=0.2, height=0.2)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file, also assign a letter to each turtle
def draw_fruit(active_turtle, image):
    active_turtle.up() # no lines please
    active_turtle.shape(image)
    active_turtle.goto(randint(-100, 100), randint(-50, 150)) # give turtle random position
    active_turtle.write(letters[fruits.index(active_turtle)], font=("Arial", 10, "bold"), align = "center") # write the letter assigned to this turtle

# draw all the fruit
def draw_fruits():
    for i in range(number_of_fruit):
        new_turt = trtl.Turtle() # create a turlte
        fruits.append(new_turt) # add this turtle to the list of fruits
        if (randint(0, 1)):# pick fruit type and draw it
            draw_fruit(new_turt, apple_image)
        else:
            draw_fruit(new_turt, pear_image)
    wn.update()

# drop the apple
def drop_fruit(fruit):
    fruit.clear()
    fruit.goto(fruit.xcor(), -100)
    fruits.remove(fruit)

#--key pressed functions
def a_pressed():
   letter_pressed("a")
def s_pressed():
    letter_pressed("s")
def d_pressed():
    letter_pressed("d")
def f_pressed():
    letter_pressed("f")
def g_pressed():
    letter_pressed("g")
def h_pressed():
    letter_pressed("h")
def j_pressed():
    letter_pressed("j")
def k_pressed():
    letter_pressed("k")
def l_pressed():
    letter_pressed("l")

def letter_pressed(string): # match key pressed to fruit to drop and remove the first instance from the list
    for letter in letters:
        if letter == string:
            drop_fruit(fruits[letters.index(string)])
            letters.remove(string)
            return


#-----setup functions-----
# get keypresses based on letters assigned
def setup_keypresses():
    for i in range(0, len(letters)):
        function = get_keypress_function(letters[i])
        wn.onkeypress(function, letters[i])

# get the function dependent on the letter given
def get_keypress_function(letter):
    letter = letter.lower()
    match letter:
        case "a":
            function = a_pressed
        case "s":
            function = s_pressed
        case "d":
            function = d_pressed
        case "f":
            function = f_pressed
        case "g":
            function = g_pressed
        case "h":
            function = h_pressed
        case "j":
            function = j_pressed
        case "k":
            function = k_pressed
        case "l":
            function = l_pressed
    return function
        
# get random letters in the currently availible letters
def randomize_letters():
    for i in range(number_of_fruit):
        j = randint(0,len(availible_letters)-1)
        letters.append(availible_letters[j])
    wn.tracer()

#-----function calls-----
randomize_letters()
setup_keypresses()
wn.tracer(False) # remove movement and wasted time at the beginning of the program
draw_fruits()
wn.bgpic("background.gif")
wn.tracer(True) # start tracer back up before listen function
wn.listen() # starts the "game"
wn.mainloop()