# Basketball thing
# coded by: jsk & hk
import turtle
import time
import random

#Turtle tester
placeholder = turtle.Turtle()

# Setup screen
window = turtle.Screen()
window.setup(1000, 1000)

#add object types to screen
ball = "ball.gif"
hoop = "hoop.gif"
window.addshape(ball)
window.addshape(hoop)

#-----Global Variables-----
valid_angles = [35, 45, 55, 65]
number_of_balls = 5  #number of tries at getting the basket
game_running = False  #is the game in progress
program_online = True  #whether or not the program will actually start the game
basketball_start = (-500, -500
                    )  #@hk105 here to change basketball starting position
timer = 0  #for power of shot
active_ball = None  #currently active ball


#-----Helper funcitons-----
def button_hit(x, y, button):
  """
    return true if the defined button area includes coordinate (x,y)\n
    STUB: returns true
    """
  return True


def create_balls(x):
  """
    create x turtles,
    hide them, 
    move them to starting position,
    give them random starting angles,
    then return them all as an array
    """
  balls = []
  for i in range(5):
    new_turt = turtle.Turtle()
    new_turt.up()
    new_turt.speed(0)
    new_turt.hideturtle()
    new_turt.setheading(0 + valid_angles[random.randint(0, 3)])
    new_turt.goto(basketball_start)
    new_turt.shape(ball)
    balls.append(new_turt)
  return balls


def pick_ball_path():
  """
    takes the current ball and shoots it
    based on it's heading and how long the shot was wound up\n
    STUB: returns nothing
    """
  global active_ball, timer
  print(timer, "DONE")
  window.onkeypress(do_nothing, "space")
  return


def start_on_click(x, y):
  """starts the game if the window is clicked in the c"""
  global game_running
  if (button_hit(x, y, "START")):
    start_game()
  game_running = False


def do_nothing(x, y):
  """placeholder function for onclick for turtle requiring function paramater\n
  does absolutely nothing"""
  return

def do_nothing():
  """placeholder function for onkeypress for turtle requiring function paramater\n
  does absolutely nothing"""
  return
  

#-----Game Events-----
def display_menu():
  """displays directions for game and start button, also calls start_game() once it completes"""
  #menu system goes here
  menu_turt = turtle.Turtle()
  menu_turt.up()
  menu_turt.goto(0, 100)
  menu_turt.write("Welcome to the Game", align='center', font=('Arial', 13, 'bold'))
  menu_turt.goto(0, 0)
  menu_turt.write("Game info goes here", align='center', font=('Arial', 13, 'normal'))
  #onclick  
  window.onclick(start_on_click)
  window.listen()


def start_game():
  """setups the game for play \n
    changes inputs to fit the gameplay"""
  global active_ball
  #clear window and keypress events
  window.clear()
  window.onclick(do_nothing)

  #put basketball and hoop in correct locations
  setup_hoop()
  balls = create_balls(number_of_balls)
  for ball in balls:
    active_ball = ball
    ball.showturtle()
    window.onkeypress(begin_shot, "space")


def setup_hoop():
  """moves the hoop into the correct position dependant on the current screen size
      STUB"""
  global hoop
  turt = turtle.Turtle()
  turt.up()
  turt.goto(60, 60)
  turt.shape(hoop)
  return


def begin_shot():
  """start a timer for the power of this next shot"""
  global timer, after_id
  if (timer<5) and (timer>0):
    turtle.getcanvas().after_cancel(after_id) #cancel previous ontimer/after event

  timer += 0.1
  print(timer)
  after_id = turtle.getcanvas().after(500, end_shot) #wait for a bit before doing end_shot so more input can be used
  
  


def end_shot():
  """end the timer and shoot the ball"""
  global timer
  timer = 0
  pick_ball_path()



#-----Setup-----#

display_menu()

window.mainloop()
