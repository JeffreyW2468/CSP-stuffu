
#adjust background color and dimensions
import turtle as trtl
wn = trtl.Screen()
wn.title("Python Snake")
wn.bgcolor("black")
wn.setup(width = 900, height = 800)

#create snake body and move to starting location
snake = trtl.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(4)
snake.hideturtle()
snake.penup()
snake.goto(-300,-300)
snake.showturtle()

#Apples
x = -300
y = 300
apples = trtl.Turtle()
apples.speed(0)
apples.shape("circle")
apples.shapesize(0.5,0.5)
apples.color("red")
apples.penup()
apples.goto(x,y)

#main loop
iteration = 0
while (iteration < 6):
    snake.left(90)
    snake.forward(600)
    #Collision
    if (abs(apples.xcor() - snake.xcor()) < 5):
        if (abs(apples.ycor() - snake.ycor()) < 5):
            x += 110
            apples.goto(x,y)
    snake.right(90)
    snake.forward(10)
    snake.right(90)
    snake.forward(600)
    snake.left(90)
    snake.forward(100)
    iteration = iteration + 1
 
#final movement before wall
snake.left(90)
snake.forward(600)
apples.hideturtle()
snake.right(90)
snake.forward(10)
snake.right(90)
snake.forward(600)
snake.left(90)
snake.forward(60)

 # Check for a collision with the border
if snake.xcor()>400 or snake.xcor()<-450 or snake.ycor()>400 or snake.ycor()<-400:
    snake.direction = "stop"
    snake.fillcolor("gray")
    snake.pencolor("red")
    # Display death prompt
    snake.hideturtle()
    snake.goto(0,0)
    snake.shapesize(500)
    snake.fillcolor("white")
    snake.write("Game Over! You Died!", font=("Arial", 20, "bold"))


wn.mainloop()