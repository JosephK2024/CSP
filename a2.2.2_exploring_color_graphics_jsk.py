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
painter.pencolor(color_hex)

#draw line
y = 0
painter.forward(40)

#set color for line
color_r = 0
color_g = 0
color_b = 0

color_hex_values.pop(0)
print(color_hex_values)

for i in range(0,len(color_hex_values)):
    hex_value = color_hex_values[i]
    if (i == 0) | (i == 2) | (i == 4):
        place_val = 16
    elif (i == 1) | (i == 3) | (i == 5):
        place_val = 1
    
    if  (hex_value == 'A'):
        digit_val = 10
    elif (hex_value == 'B'): 
        digit_val = 11
    elif (hex_value == 'C'):
        digit_val = 12
    elif (hex_value == 'D'):
        digit_val = 13
    elif (hex_value == 'E'):
        digit_val = 14
    elif (hex_value == 'F'):
        digit_val = 15
    else:
        digit_val = int(hex_value)
    
    dec_value = digit_val*place_val


    if (i == 0) | (i == 1):
        color_r += dec_value
    elif (i == 2) | (i == 3):
        color_g += dec_value
    else:
        color_b += dec_value
    print(color_b, color_g, color_r)
    
painter.pencolor(color_r, color_g, color_b)

#move down & draw line
painter.penup()
y = y - 30
painter.goto(0,y)
painter.pendown()
painter.forward(40)

#keep the output window open
screen.mainloop()
