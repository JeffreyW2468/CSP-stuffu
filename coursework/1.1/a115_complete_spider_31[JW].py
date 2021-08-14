#   a116_buggy_image.py
import turtle as trtl

#create a spider body
spider = trtl.Turtle()

#create a spider head
spider.pensize(40)
spider.circle(20)

#configure spider legs
legs = 8
length = 70
angle = 180 / legs
spider.pensize(5)
num_legs = 0

#draw legs
while (num_legs < 4):
  spider.goto(0,20)
  spider.setheading(angle*num_legs - 36)
  spider.forward(length)
  num_legs = num_legs + 1
while (num_legs < legs):
  spider.goto(0,20)
  spider.setheading(angle*num_legs + 54)
  spider.forward(length)
  num_legs = num_legs + 1

#eyes
eyes = 1
while (eyes <= 2):
  spider.penup()
  spider.goto(-22,15)
  if (eyes > 1):
    spider.goto(15,15)
  spider.pendown()
  spider.pensize(10)
  spider.color("white")
  spider.circle(10)
  eyes = eyes + 1

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()