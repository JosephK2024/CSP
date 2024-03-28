# Basketball thing
# coded by: jsk & hk
import turtle
import  time 

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

#for testing
placeholder.shape(ball)
placeholder.shapesize(0.0001)

window.mainloop()