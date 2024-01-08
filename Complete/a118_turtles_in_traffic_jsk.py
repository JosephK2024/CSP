#   a118_turtles_in_traffic_jsk.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import math

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

#place turtles around the screen in grid pattern
tloc = 50
for s in turtle_shapes:

  # create a horizontal turtle with shape s
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  # horizontal movement
  ht.goto(0, -tloc)
  ht.setheading(0)

  # create a vertical turtle with shape s
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  # vertical movement
  vt.goto( -tloc, 0)
  vt.setheading(270)
  
  # increase distance for next turtle
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

for step in range(30):
	# do something

  # move horizontal turtles vertically
  for turtle in horiz_turtles:
    turtle.setx(turtle.xcor() - 10)
  
  # move vertical turtles horizontally
  for turtle in vert_turtles:
    turtle.sety(turtle.ycor() - 10)
  
  for turtle in horiz_turtles:
    for turtle2 in vert_turtles:
      if (turtle2.ycor() == turtle.ycor()) & (turtle2.xcor() == (turtle.xcor())):
        horiz_turtles.pop(horiz_turtles.index(turtle))
        vert_turtles.pop(vert_turtles.index(turtle2))



wn = trtl.Screen()
wn.mainloop()
