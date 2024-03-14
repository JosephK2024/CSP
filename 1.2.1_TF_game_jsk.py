import turtle as t

#----- Questions and flavor text -----#
questions = ["Sharks are mammals", "Sea otters have a favorite rock", "The blue whale is the biggest animal ever", "The hummingbird has the smallest bird egg", "Pigs roll in the mud as they don't like being clean"]
questions_answer = [False, True, True, True, False]
flavortext = ["sharks are classified as fish", "they keep these treasures in the loose skin under their arms to break open food", "and that includes dinosaurs!", "on the flip side, ostriches lay the largest eggs", "pigs have few sweat glands and their muddy baths help keep them cool"]

#----- Initialize variables -----#
score = 0
num_question = 0
defualt_font = ("Arial", 20, "normal")


#----- Create screen/window -----#
wn = t.Screen()
wn.setup(0.5, 0.5)


#----- Create turtles -----#
true_button = t.Turtle()
false_button = t.Turtle()
next_button = t.Turtle()
flavortext_writer = t.Turtle()
score_writer = t.Turtle()
question_writer = t.Turtle()


#----- Set up writers -----#
def setup_writers():
    #setup question writer
    question_writer.up()
    question_writer.goto(-400, 100)
    question_writer.hideturtle()

    #setup flavortext writer
    flavortext_writer.up()
    flavortext_writer.goto(-150, -100)
    flavortext_writer.hideturtle()

    #setup score writer
    score_writer.up()
    score_writer.goto(-10, 200)
    score_writer.hideturtle()


#----- Set up buttons -----#
def setup_buttons():
    #setup the location of the two buttons
    true_button.speed(0)
    false_button.speed(0)
    true_button.penup()
    false_button.penup()
    
    #write the button type and place the buttons
    true_button.goto(-110,-55)
    true_button.write("TRUE", font=defualt_font)
    false_button.goto(36,-55)
    false_button.write("FALSE", font=defualt_font)
    true_button.goto(-75,0)
    false_button.goto(75,0)    
    
    #setup the look of the two buttons
    true_button.shape("square")
    false_button.shape("square")
    true_button.color("green", "green")
    false_button.color("red", "red")
    true_button.shapesize(2,4,0)
    false_button.shapesize(2,4,0)

    #setup the final button 
    next_button.up()
    next_button.goto(0, 0)
    next_button.turtlesize(5)

#----- Game functions -----#
def wrap(text, space, size):
    text_c = list(text)
    wrapped_text = ""
    letters_per_row = int(space/size)
    leftovers = 0
    for snippet in range(0, int(len(text_c)/letters_per_row)):
        text_snippet = []
        for index in range(0 + (letters_per_row*snippet) - leftovers, letters_per_row*(snippet+1) - leftovers):
            text_snippet.append(text_c[index])
        leftovers = 0
        space_index = text_snippet.index(" ")
        if(space_index == -1):
            return wrap(text_c, space, size - 1)
        while (space_index != len(text_snippet)):
            text_snippet.pop()
            leftovers += 1
        for index in range(0, len(text_snippet)):
            wrapped_text += str(text_snippet[index])
        wrapped_text += "\n"
    
    return wrapped_text, size

def true_clicked(x, y):
    print_flavor_text(True)

def false_clicked(x, y):
    print_flavor_text(False)

def print_flavor_text(answer):
    global score, num_question
    if (answer == questions_answer[num_question]):
        addition = "Correct! "
        score += 1
    else:
        addition = "Wrong... "
    
    wrapped_text = wrap(addition + flavortext[num_question], 300, 20)
    flavortext_writer.write(wrapped_text[0], font=("Arial", wrapped_text[1], "normal"))

    false_button.hideturtle()
    false_button.clear()
    true_button.hideturtle()
    true_button.clear()
    next_button.showturtle()
    next_button.write("Next", font=defualt_font)


def next_question(x, y):
    global num_question
    num_question += 1
    if (num_question >= len(questions)):
        num_question = len(questions) -1 
        end()
    else:
        update_turtles()
        
def end():
    global score
    #clear all buttons and writers
    false_button.hideturtle()
    false_button.clear()
    true_button.hideturtle()
    true_button.clear()
    flavortext_writer.clear()
    question_writer.clear()
    next_button.hideturtle()
    next_button.clear()
    score_writer.clear()

    #write ending message
    question_writer.write("End, your score: " + str(score), font=defualt_font)

def update_turtles():
    global score
    #clear all text (and next button)
    flavortext_writer.clear()
    question_writer.clear()
    next_button.hideturtle()
    next_button.clear()
    score_writer.clear()
    
    #write new text
    wrapped_text = wrap(questions[num_question], 800, 40)
    question_writer.write(wrapped_text[0], ("Arial", wrapped_text[1], "normal"))
    score_writer.write(score)
    
    #show T/F buttons
    true_button.showturtle()
    false_button.showturtle()
    

#----- Create Events -----#
false_button.onclick(false_clicked)
true_button.onclick(true_clicked)   
next_button.onclick(next_question)

#----- Begin Game -----#
setup_buttons()
setup_writers()

update_turtles()
wn.mainloop()