#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  
# starting point of the movement
startx = 0
starty = 0

# direction and placement of the shapes
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  angle = 20
  t.setheading(angle + 20)
  t.right(45)
  t.forward(50)
  t.pendown()
  startx = t.xcor()
  starty = t.ycor()
# new position
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()