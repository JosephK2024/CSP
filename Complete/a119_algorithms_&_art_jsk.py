# a119_algorithms_&_art_jsk.py
# Description: Uses turtles to create a
#              screensaver that includes
#              bouncing objects
# Coder: Joseph K
# Start Date: January 9th(?) 2023

DEBUG = False

import turtle
import random
if (DEBUG):
    from time import sleep
from math import sqrt


#What shapes will be used in the program
shape_list = ['circle', 'square']

#What colors will be used in the program
colors = ['red', 'blue', 'green']

#What size of screen to initialize at
width = 1000
height = 1000

#How many times the objects will move
rounds = 100


screen = turtle.Screen()

def start(obj_num):
    #initialize arrays
    objects = []

    #Initialize screen
    screen.setup(width, height)

    if (DEBUG):
        #for later checking
        ixvelocity = 0
        iyvelocity = 0
        fxvelocity = 0
        fyvelocity = 0

    #Loop through to create each object
    for i in range(obj_num):

        if (DEBUG):
            #print number of objects made so far
            print(i + 1)

        #Create new object
        obj = turtle.Turtle()
        obj.shape(shape_list[i%shape_list.__len__()])
        obj.color(colors[i%colors.__len__()])

        #hide traces before movement
        obj.hideturtle()
        obj.penup()
        
        #Give object random velocity (x and y pair) 
        #paired for easier transfer of energy  
        obj_velocity = [random.randint(-10, 10), random.randint(-10, 10)]
        
        #Give object random coordinates within screen
        obj_coords = [random.randrange(-(screen.window_width()/2) + 20,
                                        (screen.window_width()/2) - 20),
                       random.randrange(-(screen.window_height()/2) + 20,
                                         (screen.window_height()/2) - 20)]
        obj.goto(obj_coords) #goto coordinates

        
        #Add object to list
        objects.append([obj, obj_velocity])
        
        if (DEBUG):
            #for later checking
            ixvelocity += obj_velocity[0]
            iyvelocity += obj_velocity[1]

    simulate(objects)
    screen.mainloop()

    if (DEBUG):
        #somehow not an elastic collision????
            #the walls change energy into it's inverse
                #only part of the problem
        for obj in objects:
            fxvelocity += obj[1][0]
            fyvelocity += obj[1][1]
        print(fxvelocity == ixvelocity & fyvelocity == iyvelocity)
        print(fxvelocity, ixvelocity)
        print(fyvelocity, iyvelocity)

def simulate(objects):
    if (DEBUG):
        print("simulation start")

    #Show object and ensure by sheer randomness that 2 objects will not overlap
        #program should fail regardless if 
            #there are too many objects
            #the screen is too small
        #TODO: nice to have; ensure they will never overlap
    for obj in objects:
        obj[0].showturtle()
        obj[0].goto(obj[0].xcor() - obj[1][0], obj[0].ycor() - obj[1][1])

    #Simulate rounds
    for i in range(0, rounds):

        for obj in objects:
            #Goto instead of forward for smoothness of velocity pairs
            obj[0].goto(obj[0].xcor() - obj[1][0],
                         obj[0].ycor() - obj[1][1])
            
            if (DEBUG):
                print("moving", obj) 

            #check if any bouncing is needed and bounce if so
            bouncing(obj1 = obj, objects = objects)

    if (DEBUG):
        print("end")
    
    return

def bouncing(obj1, objects):
    #Bounce objects away from wall
    if ((-screen.window_height()/2 >= (obj1[0].ycor() - 20)) |
         ((obj1[0].ycor() + 20) >= screen.window_height()/2)): #top/bottom
        if((-screen.window_height()/2 >= obj1[0].ycor()) |
            (obj1[0].ycor() >= screen.window_height()/2)):#out of bounds
            obj1[0].setpos(obj1[0].xcor(), 0)

            if (DEBUG):
                print("OUT OF BOUNDS")

        #switch y velocity
        obj1[1][1] = -obj1[1][1]

        if (DEBUG):
            print(obj1, "hit screen top/bottom, bouncing")
            sleep(2)
    if ((-screen.window_width()/2 >= (obj1[0].xcor() - 20)) |
         ((obj1[0].xcor() + 20) >= screen.window_width()/2)):#sides
        if((-screen.window_width()/2 >= obj1[0].xcor()) |
            (obj1[0].xcor() >= screen.window_width()/2)):#out of bounds
            #goto place where others are likely not
            obj1[0].setpos(0, obj1[0].ycor())

            if (DEBUG):
                print("OUT  OF BOUNDS")

        #switch x velocity
        obj1[1][0] = -obj1[1][0]
        
        if (DEBUG):
            print(obj1, "hit screen side, bouncing")
            sleep(2)

    #Bounce objects off eachother
    for obj2 in objects:
        if (obj2 != obj1):#not the same object
            if(sqrt(pow(obj1[0].xcor() - obj2[0].xcor(), 2)
                    + pow(obj1[0].ycor() - obj2[0].ycor(), 2))
                    <= 10*(obj1[0].pensize() + obj2[0].pensize())):
                
                if (DEBUG):
                    print(obj1, obj2, "collision")

                #move the objects as they should
                collide(obj1=obj1, obj2=obj2)
            
    
def collide(obj1, obj2):
    #TODO: nice to have;figure out how to seamlessly transfer energy from one
    #^object to another
    vph = 0 #placeholder velocity
    
    if (DEBUG):
        print('y',abs(obj1[0].ycor() - obj2[0].ycor()) > 5,
               '\nx', abs(obj1[0].xcor() - obj2[0].xcor()) > 5)
    
    #find side it bounced on
    if (abs(obj1[0].ycor() - obj2[0].ycor()) > 5):
        #switch y velocity of objects
        vph = obj1[1][1]
        obj1[1][1] = obj2[1][1]
        obj2[1][1] = vph
        
        if (DEBUG):
            print("y change")

    if (abs(obj1[0].xcor() - obj2[0].xcor()) > 5):
        #switch x velocity of objects
        vph = obj1[1][0]
        obj1[1][0] = obj2[1][0]
        obj2[1][0] = vph
        if (DEBUG):
            print("x change")
    
    obj1[0].goto(obj1[0].xcor() - obj1[1][0], obj1[0].ycor() - obj1[1][1])
    obj2[0].goto(obj2[0].xcor() - obj2[1][0], obj2[0].ycor() - obj2[1][1])
    
    if (DEBUG):
        print("BANG!")
        sleep(2)


#start the code
start(20)