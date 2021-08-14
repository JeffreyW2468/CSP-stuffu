#initialization
import turtle as trtl
'''pea_shooter = trtl.Turtle()
pea_shooter = "peashooter.gif"
wn.addshape(pea_shooter)'''

#function defs
def start_game():
    wn = trtl.Screen()
    wn.bgpic("/Applications/VSC/Python/Hello_world/CSP/1.3.1_project/pvz_bg.gif")
    wn.mainloop()
    

#function calls
start_game()



'''#initialization
import turtle as trtl
wn = trtl.Screen()
wn.setup(height=1.0, width=1.0)
pea_shooter = "peashooter.gif"
wn.addshape(pea_shooter)
trtl.shape(pea_shooter)

#function defs
pea_shooter = trtl.Turtle()
pea_shooter.penup()
pea_shooter.goto(-300,300)


#function calls
wn.bgpic("grass.gif")

wn.mainloop()'''