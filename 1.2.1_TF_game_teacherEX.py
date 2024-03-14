# Activity 1.2.1 True-False Quiz
# Description: User answers 5 true-false questions to try for
#              the best score
# Coder(s): Dennis Michaud
# Date: March 8, 2024

#----- import necessary modules -----
import turtle, csv, random

#----- global variables & game configuration -----

#use turtle objects for user to select true or false
true_button = turtle.Turtle()
false_button = turtle.Turtle()

#use turtle objects to write out the questions, responses, score, and timer
question_writer = turtle.Turtle()
response_writer = turtle.Turtle()
score_writer = turtle.Turtle()
timer_writer = turtle.Turtle()

#set up game window 
window_size_x = 640
window_size_y = 480
screen = turtle.Screen()
screen.setup(window_size_x, window_size_y)

# constants
number_questions = 5
counter_interval = 1000

# global variables
question_live = False
question_number = 0
questions = []
question_answers = []
question_responses = []
score = 0
timer = 5

#----- game functions -----

# setup the True and False "buttons"
def initialize_TF_buttons():
   
   #setup the location of the two buttons
   true_button.speed(0) #fastest movement
   false_button.speed(0) #fastest movement
   true_button.penup()
   false_button.penup()

   #write the button type and place the buttons
   true_button.goto(-110,-55)
   true_button.write("TRUE", font=("Arial", 20, "normal"))
   false_button.goto(36,-55)
   false_button.write("FALSE", font=("Arial", 20, "normal"))
   true_button.goto(-75,0)
   false_button.goto(75,0)
   
   #setup the look of the two buttons
   true_button.shape("square")
   false_button.shape("square")
   true_button.color("green", "green")
   false_button.color("red", "red")
   true_button.shapesize(2,4,0)
   false_button.shapesize(2,4,0)

# setup the question, response, and score writer turtles
def initialize_writers():

   #question writer setup
   question_writer.hideturtle()
   question_writer.penup()
   question_writer.speed(0)
   question_writer.goto(0, 50)
 
   #response writer setup
   response_writer.hideturtle()
   response_writer.penup()
   response_writer.speed(0)
   response_writer.goto(0, -80)

   #score writer setup
   score_writer.hideturtle()
   score_writer.penup()
   score_writer.speed(0)
   score_writer.goto(200, 160)

   #timer writer setup
   timer_writer.hideturtle()
   timer_writer.speed(0)
   timer_writer.penup()
   timer_writer.goto(-200, 160)

#creates a set of T/F questions, answers, and responses
def setup_question_lists():

   #fetch data from file
   file = open("a1.2.2TFQuestionDatabase.csv", "r")
   data = list(csv.reader(file, delimiter=","))
   file.close()

   for n in range(0, 5):
      index = random.randint(0, len(data))
      questions.append(data[index][0])
      question_answers.append(data[index][1] == "TRUE")
      question_responses.append(data[index][2])

# wait for the user to continue the game
def wait_for_user():

   #different behavior at the start of the game versus during
   if (question_number == 0):
      instructions = "Click on the True button to start"
   elif (question_number < number_questions):
      instructions = "Click on the True button to continue"
   else:
      instructions = "Game over, click anywhere to exit"

   question_writer.clear()
   question_writer.write(instructions, 
                         move=False, align="center", 
                         font=("Arial", 12, "normal"))

   if (question_number < number_questions):
      true_button.onclick(continue_game)
   else:
      screen.exitonclick()

# determines the font size of questions & responses so that they
# fit on one line
def determine_font_size(text):

   font_size = 12
   if (len(text) > 60):
      font_size = round(18 - 0.09 * len(text))

   return font_size

# display a new T/F question and wait for response.
def ask_question():

   global question_live

   question_text = questions[question_number - 1]
   #adjust font size to fit into 1 line
   font_size = determine_font_size(question_text)

   question_writer.clear()
   response_writer.clear()
   question_writer.write(question_text, 
                         move=False, align="center", 
                         font=("Arial", font_size, "normal"))
   
   #link clicking on T/F buttons to their events
   true_button.onclick(true_clicked)
   false_button.onclick(false_clicked)

   question_live = True
   
# display the player's score
def display_score():

   score_writer.clear() #erase any previous score
   score_writer.write("Score: " + str(score), 
                      move=False, align="left", 
                      font=("Arial", 12, "normal"))

# display a new T/F question 
def report_response(answer_given):

   global score, timer

   #determine if correct or incorrect
   correct_response = question_answers[question_number - 1]
   if (answer_given == correct_response):
      response_text = "Correct, the statement was " + str(correct_response)
      score += int(100*timer/30)
   else:
      response_text = "Sorry, the statement was " + str(correct_response)

   #add rest of response text about the question
   response_text += " -- " + question_responses[question_number - 1]

   #adjust font size to fit into 1 line
   font_size = determine_font_size(response_text)
   
   response_writer.clear()
   response_writer.write(response_text, 
                         move=False, align="center", 
                         font=("Arial", font_size, "normal"))
   display_score()
   
#----- game event functions -----

#event code when true button is clicked to start/continue game
def continue_game(x, y):

   global question_number
   question_number += 1

   ask_question()

   #link clicking on T/F buttons to their events
   true_button.onclick(true_clicked)
   false_button.onclick(false_clicked)

   #begin countdown
   screen.ontimer(countdown, counter_interval)

#event code when true button is clicked during game
def true_clicked(x, y):
   
   global question_live
   
   if question_live:
      question_live = False
      report_response(True)
      wait_for_user()
      
 #event code when false button is clicked during game
def false_clicked(x, y):

   global question_live

   if question_live:
      question_live = False
      report_response(False)
      wait_for_user()

def countdown():
   global timer, question_live
   if question_live:
      timer_writer.clear()
      if timer <= 0:
         question_live = False
         report_response(None)
         wait_for_user()
      else:
         timer_writer.write("Timer: " + str(timer), font = ("Arial", 12, "normal"))
         timer -= 1
         timer_writer.getscreen().ontimer(countdown, counter_interval)
   else:
      timer = 30


#----- run the game -----

#setup the game
initialize_TF_buttons()
initialize_writers()
setup_question_lists()
wait_for_user()

#keeps the game window active
screen.mainloop()