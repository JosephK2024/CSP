import turtle
import random
from time import sleep

#What shapes will be used in the program
shape_list = ['circle', 'square']

#What size of screen to initialize at
width = 1000
height = 1000

def start(obj_num):
    #initialize arrays
    obj_descriptors = []

    #Initialize screen
    screen = turtle.Screen()
    screen.setup(width, height)

    #Loop through to create each object
    for i in range(obj_num):
        print(i)
        #Create new object
        obj = turtle.Turtle()
        obj.shape(shape_list[i%shape_list.__len__()])
        obj.hideturtle()
        obj.penup()
        
        #Give object random velocity
        obj_velocity = random.randint(-5, 5)
        
        #Give object random coordinates within screen
        obj_coords = [random.randrange(-(screen.window_width()/2),screen.window_width()/2), random.randrange(-(screen.window_height()/2),screen.window_height()/2)]
        obj.goto(obj_coords)
        
        obj_descriptors.append([obj, obj_velocity])


    test(obj_descriptors)
    simulate(obj_descriptors)
    


def simulate(turtle_list, start_velocity):
    return

def test(turtle_list):
    print("got to test")
    for obj in turtle_list:
        obj[0].showturtle()
    screen = turtle.Screen()
    screen.mainloop()
    


#start
start(15)