import turtle
import random
from time import sleep #Used for debugging purposes
from math import sqrt

#What shapes will be used in the program
shape_list = ['circle', 'square']

#What size of screen to initialize at
width = 1000
height = 1000

screen = turtle.Screen()

def start(obj_num):
    #initialize arrays
    objects = []

    #Initialize screen
    screen.setup(width, height)

    #Loop through to create each object
    for i in range(obj_num):
        print(i)
        #Create new object
        obj = turtle.Turtle()
        obj.shape(shape_list[i%shape_list.__len__()])
        obj.hideturtle()
        obj.penup()
        
        #Give object random velocity (x and y pair) paired for easier transfer of energy  
        obj_velocity = [random.randint(-10, 10), random.randint(-10, 10)]
        
        #Give object random coordinates within screen
        obj_coords = [random.randrange(-(screen.window_width()/2) + 20, (screen.window_width()/2) - 20), random.randrange(-(screen.window_height()/2) + 20, (screen.window_height()/2) - 20)]
        obj.goto(obj_coords) #goto coordinates

        
        #Add object to list
        objects.append([obj, obj_velocity, False])


    #test(objects)
    simulate(objects)
    


def simulate(objects):
    print("simulation start")

    #Show object and ensure by sheer randomness that 2 objects will not overlap
        #program should fail regardless if there are enough objects or the screen is too small
        #TODO: nice to have; ensure they will never overlap
    for obj in objects:
        obj[0].showturtle()
        obj[0].goto(obj[0].xcor() - obj[1][0], obj[0].ycor() - obj[1][1])

    #Simulate 100 times
    for i in range(0, 1000):

        for obj in objects:
            obj[2] = False
            #Goto instead of forward for smoothness of velocity pairs
            obj[0].goto(obj[0].xcor() - obj[1][0], obj[0].ycor() - obj[1][1])
            print("moving", obj) 
            bouncing(obj1 = obj, objects = objects)

    print("end")
    screen.mainloop()

def test(objects):
    return
    

def bouncing(obj1, objects):
    #Bounce objects away from wall
    if ((-screen.window_height()/2 >= (obj1[0].ycor() - 20)) | ((obj1[0].ycor() + 20) >= screen.window_height()/2)):
        if((-screen.window_height()/2 >= obj1[0].ycor()) | (obj1[0].ycor() >= screen.window_height()/2)):
            obj1[0].setpos(obj1[0].xcor(), 0)
            print("OUT OF BOUNDS")
        obj1[1][1] = -obj1[1][1]
        print(obj1, "hit screen top/bottom, bouncing")
        #sleep(2)
    if ((-screen.window_width()/2 >= (obj1[0].xcor() - 20)) | ((obj1[0].xcor() + 20) >= screen.window_width()/2)):
        if((-screen.window_width()/2 >= obj1[0].xcor()) | (obj1[0].xcor() >= screen.window_width()/2)):
            obj1[0].setpos(0, obj1[0].ycor())
            print("OUT  OF BOUNDS")
        obj1[1][0] = -obj1[1][0]
        print(obj1, "hit screen side, bouncing")
        #sleep(2)

    #Bounce objects off eachother
    for obj2 in objects:
        if (obj2 != obj1):
            if(sqrt(pow(obj1[0].xcor() - obj2[0].xcor(), 2) + pow(obj1[0].ycor() - obj2[0].ycor(), 2)) <= 10*(obj1[0].pensize() + obj2[0].pensize())):
                print("pow?")
                collide(obj1=obj1, obj2=obj2)
            
    
def collide(obj1, obj2):
    #TODO: nice to have;figure out how to seamlessly transfer energy from one object to another
    print("BANG!")
    #find side it bounced on
    objph = ["turtle", [2, 3]] #placeholder
    print('y',abs(obj1[0].ycor() - obj2[0].ycor()) > 10, '\nx', abs(obj1[0].xcor() - obj2[0].xcor()) > 10)
    if (abs(obj1[0].ycor() - obj2[0].ycor()) > 5):
        objph = obj1
        obj1[1][1] = obj2[1][1]
        obj2[1][1] = objph[1][1]
        obj1[2] = True
    if (abs(obj1[0].xcor() - obj2[0].xcor()) > 5):
        objph = obj1
        obj1[1][0] = obj2[1][0]
        obj2[1][0] = objph[1][0]
        obj1[2] = True
    sleep(2)
    obj1[0].goto(obj1[0].xcor() - obj1[1][0], obj1[0].ycor() - obj1[1][1])
    obj2[0].goto(obj2[0].xcor() - obj2[1][0], obj2[0].ycor() - obj2[1][1])



#start
start(10)