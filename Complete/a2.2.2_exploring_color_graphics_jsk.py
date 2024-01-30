#Python program exploring changing line colors

import turtle

#create painter turtle
painter = turtle.Turtle()
painter.pensize(5)
painter.hideturtle()
screen = painter.getscreen()
screen.colormode(255) #allows setting colors using RBG values

#set up repeat vars
repeat = True
y = 0

while(repeat):
    #set color for line
    color_hex = input("The next hex value: #") #get user input
    color_hex_values = list(color_hex)

    #check for hashtags
    if(color_hex[0] == '#'):
        color_hex_values.pop(0)

    #set color for line
    color_r = 0
    color_g = 0
    color_b = 0

    for i in range(0,len(color_hex_values)): #do all of the values at once for fun :3
        hex_value = color_hex_values[i]

        # find digits place value
        if (i == 0) | (i == 2) | (i == 4):
            place_val = 16
        elif (i == 1) | (i == 3) | (i == 5):
            place_val = 1

        # get digit value in base 10
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

        # multiply digit value by its place value to get digits "true" value
        dec_value = digit_val*place_val

        # add final value for digit to correct rgb value
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

    repeat = False 
    if (input("Again?(y/n)") == 'y'):
        repeat = True

#keep the output window open
screen.mainloop()
