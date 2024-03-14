# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand


#-----game configuration----
shape = "triangle"
color = "blue"
size = 4

score = 0

font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000 # 1000 rep 1 sec
timer_up = False


#-----initialize turtles-----
bob = t.Turtle()
bob.goto(rand.randint(-20,20), rand.randint(-20,20))
bob.shapesize(4)
bob.shape(shape)
bob.fillcolor(color)
bob.up()

score_writer = t.Turtle()
score_writer.hideturtle()
score_writer.up()
score_writer.goto(0, 501)
score_writer.down()

counter = t.Turtle()
counter.hideturtle()
counter.up()
counter.goto(501, 501)
counter.down()

#-----initialize screen/window-----
wn = t.Screen()
wn.bgcolor("orange")
wn.setup(0.4, 0.51)
wn.bgcolor("purple")

#-----game functions--------
def clicked(x, y):
    if(timer_up == False):
        update_score()
        change_position()
    else:
        bob.hideturtle()

def change_position():
    bob.hideturtle()
    bob.goto(rand.randint(-500, 500), rand.randint(-500, 500))
    bob.showturtle()

def update_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.write(score, font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font = font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font = font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def start_game():
    global wn, bob
    bob.onclick(clicked) 
    wn.ontimer(countdown, counter_interval)
    wn.mainloop()

#-----events----------------

start_game()