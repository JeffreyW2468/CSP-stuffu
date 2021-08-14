import turtle as trtl
import random

#set up screen 
wn = trtl.Screen()
wn.setup(height=1.0, width=1.0)
wn.title("Plant v. Zombies Game")


#initialization
pea_shooter = "peashooter.gif"
wn.addshape(pea_shooter)
wn.bgpic("pvzbackground.gif")


#register shapes
zombie_list = ["zombie.gif", "zombie2B.gif", "zombie3B.gif", "zombie4B.gif", "zombie5B.gif"]
zombie_group = []

def change_location(zombie):
   zombie.hideturtle() 
   zombie.penup()
   zombie.speed(0)
   x = random.randint(-300, 300)
   y = random.randint(0, 300)
   zombie.goto(x, y)
   zombie.showturtle() 

how_many = random.randint(1, len(zombie_list))

for x in range(how_many):
   trtl.register_shape(zombie_list[x])
   new_zombie = trtl.Turtle()
   new_zombie.hideturtle()
   new_zombie.shape(zombie_list[x])
   zombie_group.append(new_zombie)
   change_location(new_zombie)

#score
score = 0
write_score = trtl.Turtle()
write_score.speed(0)
write_score.color("white")
write_score.penup()
write_score.goto(-700, 300)
scorestring = "Score: %s" %score
write_score.write(scorestring, False, align="left", font=("Arial", 35, "normal"))
write_score.hideturtle()

#countdown writer
timer = 30
counter_interval =1000  
timer_up = False
counter = trtl.Turtle()
counter.color("white")
counter.hideturtle()
counter.penup()
counter.goto(600,300)
counter.pendown()
font_setup=("Arial", 35, "normal")

def end_game():
    writer2 = trtl.Turtle()
    writer2.hideturtle()
    writer2.penup()
    writer2.goto(600,300)
    writer2.color("white")
    writer2.write("Time's Up", font=font_setup)
    timer_up = True
    writer2.hideturtle()
    writer2.penup()
    writer2.goto(-150,-50)
    writer2.color("red")
    writer2.write("End Game", font=("ariel", 100, "normal"))
    wn.onkeypress(None, 'Up')
    wn.onkeypress(None, 'Down')
    wn.onkeypress(None, 'space')

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
      end_game()
    else:
     counter.write("Timer: " + str(timer), font=font_setup)
     timer -= 1
     counter.getscreen().ontimer(countdown, counter_interval)

#set zombie location to random 
number_of_zombies = len(zombie_group)
zombie_total = []

#function defs
pea_shooter = trtl.Turtle()
pea_shooter.penup()
pea_shooter.hideturtle()
pea_shooter.goto(-525,300)
pea_shooter.shape("peashooter.gif")
pea_shooter.showturtle()

pea = trtl.Turtle()
pea.shape('circle')
pea.penup()
pea.speed('fastest')
pea.shapesize(2,2,10)
pea.color('yellow')
pea.hideturtle()

def move_pea_shooter():
    pea_shooter.forward(10)



# event handlers for changing direction
def go_up():
    pea_shooter.setheading(90)
    move_pea_shooter()

def go_down():
    pea_shooter.setheading(270)
    move_pea_shooter()

def redraw_hidden_zombies():
    for one_zombie in zombie_group:
        if not one_zombie.isvisible():
            change_location(one_zombie)

def check_for_collision():
    did_collide = False
    for one_zombie in zombie_group:
        if one_zombie.isvisible() and (abs(pea.xcor() - one_zombie.xcor()) < 45 and abs(pea.ycor() - one_zombie.ycor()) < 55):
            one_zombie.hideturtle()
            global score
            write_score.clear()
            score+=1
            write_score.write("Score:" + str(score), False, align="left", font=("Arial", 35, "normal"))
            did_collide = True
    return did_collide

#NEW STUFF    
def zombie_movement():
    new_zombie.setheading(180)
    new_zombie.forward()
         
def shoot():
    pea.goto(x=pea_shooter.xcor(), y=pea_shooter.ycor())
    pea.showturtle()
    pea.setheading(0)
    while pea.xcor() < wn.screensize()[0]*1.3:
        pea.forward(10)
        if check_for_collision() == True:
            break    
    pea.hideturtle()
    redraw_hidden_zombies()
    
def write_name():
    writer = trtl.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-100,270)
    writer.color("white")
    writer.write("Welcome "+ player + "!", font=font_setup)
    writer.pendown()
    
# listen for events
player = input('Enter your name: ')
write_name()
countdown()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(shoot, 'space')
wn.listen()
wn.mainloop()



