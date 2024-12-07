import turtle

wn = turtle.Screen()
wn.title("Pong, Old School by @DSCHOI")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle() #lower 't' for module name(import), cap 'T' for class name
paddle_a.speed(0) #sets paddle spd (not the spd of paddle movement on scrn, but rather the animation spd)
paddle_a.shape("square") #built in shapes in turtle module (default: 20 pixels x 20 pixels)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") 
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.1
ball.dy = 0.1

#Functions
def paddle_a_up():
    y = paddle_a.ycor() #'ycor' is specific to Turtle. returns 'y' coordinate
    y += 10 #adds 20 pixels to 'y' coordinate
    paddle_a.sety(y) #sets paddle_a to new 'y' coordinate

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #in Turtle, this is to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses direction of ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1