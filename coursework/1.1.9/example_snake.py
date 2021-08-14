# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand 

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0 
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
colors = ["blue","red","green","yellow","purple","brown","black","violet"]
sizes = [1,2,3,5,8,6,7]
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)spot.shapesize(spot_size)
spot.color(spot_color)
spot.penup()
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-25,300)
score_writer.hideturtle()
countdown_writer = trtl.Turtle()
countdown_writer.hideturtle()
countdown_writer.penup()
countdown_writer.goto(-25,270)

#-----game functions--------
def color_adder():
    spot.stamp()
    spot.color(rand.choice(colors))


def shape_changer():
    spot.shapesize(rand.choice(sizes))

def change_position():
    spot.hideturtle()
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()

def update_score():
    global score
    score_writer.clear()
    score += 1
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  countdown_writer.clear()
  if timer <= 0:
    countdown_writer.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    countdown_writer.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    countdown_writer.getscreen().ontimer(countdown, counter_interval) 

def spot_clicked(xcor,ycor):
  global timer 
  global timer_up
  global spot_color
  spot.color(spot_color)
  if timer_up == False:
    update_score()
    color_adder()
    shape_changer()
    change_position()
  else:
    countdown_writer.hideturtle()

def start_game():
  spot.onclick(spot_clicked)
  wn = trtl.Screen() 
  wn.bgcolor("light green")
  wn.ontimer(countdown, counter_interval) 
  wn.mainloop()

#-----events----------------
start_game()