# Basketball thing
# coded by: jsk & hk
import turtle
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
basketball_start = (-200, -200
                    )  #@hk105 here to change basketball starting position
timer = 0  #for power of shot
active_ball = None  #currently active ball
balls = []


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
  for i in range(x+1): #+1 so program doesn't end before last ball is sent
    new_turt = turtle.Turtle()
    new_turt.up()
    new_turt.speed(0)
    new_turt.hideturtle()
    new_turt.setheading(0 + valid_angles[random.randint(0, 3)])
    new_turt.goto(basketball_start)
    new_turt.shape(ball)
    balls.append(new_turt)
  return balls


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

def do_nothing2():
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
  window.onkeypress(exit, "BackSpace")
  window.listen()


def start_game():
  """setups the game for play \n
    changes inputs to fit the gameplay"""
  global active_ball, balls
  #clear window and keypress events
  window.clear()
  window.onclick(do_nothing)

  #put basketball and hoop in correct locations
  setup_hoop()
  balls = create_balls(number_of_balls)

  #start the first ball
  active_ball = balls[0]
  active_ball.showturtle()
  window.onkeypress(begin_shot, "space")

    

def setup_hoop():
  """moves the hoop into the correct position"""
  global hoop
  turt = turtle.Turtle()
  turt.up()
  turt.goto(60, 60)
  turt.shape(hoop)


def begin_shot():
  """start a timer for the power of this next shot"""
  global timer, after_id
  if (timer<5) and (timer>0):
    turtle.getcanvas().after_cancel(after_id) #cancel previous ontimer/after event
  print(timer)
  timer += 0.1
  after_id = turtle.getcanvas().after(500, shoot_ball) #wait for a bit before doing the shot so more input can be done
  

def shoot_ball():
  """
    takes the current ball and shoots it
    based on it's heading and how long the shot was wound up\n
    """
  global active_ball, timer
  window.onkeypress(do_nothing2, "space")
  active_ball.speed(timer)
  active_ball.forward(100*timer)
  timer = 0
  next_ball()

def next_ball():
  """set active ball to next ball in array of balls"""
  global balls, active_ball
  i = balls.index(active_ball)
  i += 1
  try:# remove error of incrementing past array size
    active_ball = balls[i]
    active_ball.showturtle()
    window.onkeypress(begin_shot, "space")
  except:
    game_over()
  

  
def game_over():
  global game_running, balls
  game_running = False
  window.onkeypress(do_nothing2, "space")
  window.clear()
  balls = []
  display_menu()

#-----Setup-----#

display_menu()

window.mainloop()
