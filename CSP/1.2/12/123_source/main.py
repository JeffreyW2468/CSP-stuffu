#   a123_pear_1.py
import turtle as trtl

#-----setup-----
pear_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def drop_pear():
  pear.pu()
  pear.goto(0,-300)
#-----function calls-----
draw_pear(pear)
drop_pear
wn.mainloop()