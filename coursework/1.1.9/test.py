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
snake.speed(3)
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
'''
#draft of movement
segments = []
    # add a segment
new_segment = trtl.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("green")
new_segment.penup()
segments.append(new_segment)
    # move the end segment in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)
    # Move segment 0 to where the head is
if len(segments):
    x = snake.xcor()
    y = snake.ycor()
    segments[0].goto(x, y)
'''
#main loop
iteration = 0
while (iteration < 6):
    snake.left(90)
    snake.forward(600)
    #Collision
    if (abs(apples.xcor() - snake.xcor()) < 1):
        if (abs(apples.ycor() - snake.ycor()) < 1):
            x += 110
            apples.goto(x,y)
            follow = trtl.Turtle()
            follow.shape("square")
            follow.color("green")
            follow.speed(3)
            follow.setheading(follow.towards(snake))
            follow.setposition(snake.xcor(),snake.ycor())
            follow.showturtle()
    snake.right(90)
    snake.forward(10)
    snake.right(90)
    snake.forward(600)
    snake.left(90)
    snake.forward(100)
    iteration = iteration + 1
 
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

screen_prompts = []
for index in screen_prompts:
    prompt_block = trtl.Turtle()
    prompt_block[index].goto(0,0)
    prompt_block.shapesize(30)
    prompt_block.append(prompt_block)
    prompt_block.write("You Died :(")
wn.mainloop() 

