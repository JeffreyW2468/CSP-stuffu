#imports (utilizing python turtle, a rendering feature)
import turtle as trtl
import random as rand
import time
from time import sleep #utilizing time module for logging time to click and registering delays before object respawn

#initialization
trtl.Screen()
width = 950
height = 800
trtl.setup(width, height)
trtl.bgpic("sky.gif") #sets background image
trtl.title("Reaction Game")
    #shape registrations (registers various images for moving object)
trtl.addshape("coin.gif")
trtl.addshape("parrot.gif")
trtl.addshape("dragon.gif")
trtl.addshape("explosion.gif")
flying_object = trtl.Turtle()
flying_object.penup()
    #object list configuration data
object_list = ["coin.gif", "parrot.gif", "dragon.gif", "explosion.gif"] #holds the images for shape change references later
teleportation_delay = rand.randint(1, 3)
    #game timer (initializes a timer display that increments downwards by 1000 milliseconds, or exactly 1 second)
timer = 20
time_up = False
count_interval = 1000
count_display = trtl.Turtle()
count_display.speed(2)
count_display.color("black")
count_display.hideturtle()
count_display.penup()        #timer moves to the top of the screen and configures font display
count_display.goto(-320, 350)
font_config = ("Arial", 14, "normal")
    #reaction timer
time_difference = [] #stores the actual timespan between each object spawn and user response
start_time = time.time() #approximate time of when the game first begins and before the first click
flying_object.shape(str(object_list[-1])) #sets the default object appearance to explosion.gif

#functions
def response_time_report(time_difference, preference):
    average_time = round(sum(time_difference) / len(time_difference), 2) #takes the average of all response times to visual stimuli
    if preference == "average":
        count_display.write('Game over! Your average response time was: ' + str(average_time) + ' seconds!', font=font_config)
    elif preference == "holistic":
        count_display.write('Game over! Your individual response times were: ' + str([i for i in time_difference]) + ' seconds!', font=font_config) #displays each time split individually
        
def game_timer():
    global timer, time_up
    count_display.clear() 
    if timer <= 0:
        flying_object.hideturtle()
        preference = input("Would you like an average reaction time or holistic report? ")
        response_time_report(time_difference, preference) #passes previous input entry as an argument
        preference = input("You can select another report: average or holistic? ")
        count_display.clear()
        response_time_report(time_difference, preference) #calls function a second time for alternative display
        time_up = True
    else:
        count_display.write("Time: " + str(timer), font = font_config)
        timer -= 1
        count_display.getscreen().ontimer(game_timer, count_interval) #refreshes the timer display each second and updates by counting an additional second downwards to zero

def location_reset():
    x_pos = rand.randint(-475, 475)
    y_pos = rand.randint(-400, 400) #pulls random coordinates for object to travel to
    flying_object.hideturtle()
    flying_object.goto(x_pos, y_pos) #object travels to the random coordinate
    sleep(teleportation_delay) #suspends the program for a random amount of time between 1 and 3 seconds for the sake of unpredictability
    flying_object.showturtle()

def has_clicked(xcor, ycor):
    global time_up, start_time
    if time_up != True:
        time_entry = time.time() #records a timestamp of when the user clicks
        difference = round(time_entry - start_time, 2) #calculates the difference between the timestamp of the user clicking and the last timestamp where the object changed location
        time_difference.append(difference) #stores the user response time
        flying_object.shape(str(object_list[-1]))
        sleep(0.1)
        object_iteration()
        location_reset()
        start_time = time.time() #timestamps the next time that the object appears

def object_iteration():
    obj_index = rand.randint(0, 2) #random index of the object list; exclusive of the explosion animation
    flying_object.shape(str(object_list[obj_index])) #changes the object to display the random item of the object list

def run_game(): #acts as abstraction, storing the all functions necessary for running the game into one function that can be called at the end
    game_timer()
    flying_object.onclick(has_clicked)
    trtl.mainloop() #allows screen to persist after execution

#events
run_game() #calls all functions, initializing entire program

'''
Citations

coin.gif courtesy of emaze.com --> https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.emaze.com%2F%40AOTCFWIOF&psig=AOvVaw0NxqXmWRU3XUgc_4s4NOj9&ust=1621570617983000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCLDKs-K01_ACFQAAAAAdAAAAABAb
dragon.gif courtesy of tenor.com --> https://tenor.com/view/drogon-gif-21425979
explosion.gif courtesy of pinterest.com --> https://www.pinterest.com/pin/167759154858790760/
parrot.gif courtesy of Clipart Library --> http://clipart-library.com/clipart/5cRrGBAzi.htm
sky.gif courtesy of cloudygif.com --> https://www.google.com/url?sa=i&url=https%3A%2F%2Fcloudygif.com%2F84fc7fedbe4f6e1d.aspx&psig=AOvVaw0c6c0sDtWHsP4skXq4mdHl&ust=1621573747605000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCLDWzo2_1_ACFQAAAAAdAAAAABAJ

'''