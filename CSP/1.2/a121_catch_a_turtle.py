# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand 
import leaderboard as lb

#-----game configuration----
spot_color = "white"
spot_size = 2
spot_shape = "circle"
score = 0 
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000
timer_up = False
colors = ["blue","red","green","yellow","purple","brown","black","violet"]
sizes = [1,2,3,5,8,6,7]

#leaderboard variables
leaderboard_file_name = "/Users/jeff/Desktop/VSC/Python/Hello_world/CSP/1.2/a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.penup()
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(0,300)
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
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()

def update_score():
    global score
    score_writer.clear()
    score += 1
    score_writer.write(score, font=font_setup)
    
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
  
def countdown():
  global timer, timer_up
  countdown_writer.clear()
  if timer <= 0:
    countdown_writer.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
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
