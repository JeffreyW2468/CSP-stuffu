#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
 
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
 
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
 
tloc = 50
for s in turtle_shapes:
 
#top row of turtles
    #grabs a shape
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
    #uses a new random color
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
 
#bottom row of turtles
    #grabs a shape
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
    #uses a new random color
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
 
# TODO: move turtles across and down screen, stopping for collisions
 
steps = 0
while steps < 50:
    steps = steps + 1
    for ht in horiz_turtles:
      for vt in vert_turtles:
          ht.forward(3)
          vt.forward(3)
    if (abs(ht.xcor() - vt.xcor()) < 20):
                if (abs(ht.ycor() - vt.ycor()) < 20):
                    vt.fillcolor("gray")
                    vert_turtles.remove(vt)
                    ht.fillcolor("gray")
                    horiz_turtles.remove(ht) 
 
 
wn = trtl.Screen()
wn.mainloop()
