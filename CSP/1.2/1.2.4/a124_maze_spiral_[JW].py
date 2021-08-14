#   main.py
import turtle as trtl
 
#-----setup----
 
basenum = 500
ns = 25
mn = basenum/ns
maze_painter = trtl.Turtle()
maze_painter.hideturtle()
maze_painter.pencolor("black")
maze_painter.pu()()
maze_painter.goto(300,300)
maze_painter.pd()
counter = 1

 
 
#-----functions-----
def maze_looper(maze_painter, basenum, counter, mn, ns):
  while basenum != 0: 
    if(counter >= 3):
      basenum = basenum-ns
      counter = 1
    else:
      counter += 1
      maze_painter.right(90)
      maze_painter.forward(basenum)
    maze_painter.right(90)
    maze_painter.forward(10)
# given a turtle, set that turtle to be shaped by the image file
 
 
 
#-----function calls-----
wn = trtl.Screen() 
maze_looper() 
wn.mainloop()
