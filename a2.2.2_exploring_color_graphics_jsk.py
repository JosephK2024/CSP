#Python program exploring changing line colors

import turtle

#create painter turtle
painter = turtle.Turtle()
painter.pensize(5)
painter.hideturtle()
screen = painter.getscreen()
screen.colormode(255) #allows setting colors using RBG values

#set color for line
color_hex = "#DA9820"
color_hex_values = list(color_hex)
print(color_hex_values)
painter.pencolor(color_hex)

#draw line
y = 0
painter.forward(40)

#set color for line
color_r = 218
color_g = 152
color_b = 32
painter.pencolor(color_r, color_g, color_b)

#move down & draw line
painter.penup()
y = y - 30
painter.goto(0,y)
painter.pendown()
painter.forward(40)

#keep the output window open
screen.mainloop()
