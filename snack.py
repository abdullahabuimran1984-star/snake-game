import time 
import random
import turtle

delay = 0.1
score = 0
high_score = 0
#window
wn = turtle.Screen()
wn.title('Snake game')
wn.bgcolor("#61A6B9")
wn.setup(width= 600 , height= 600)
wn.tracer(0)

#snake
head = turtle.Turtle()
head.shape('square')
head.color("#E72828")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = 'Stop'


#food
food = turtle.Turtle()
shapes = random.choice(['square', 'circle'])
colors = random.choice(['red', 'green', 'black', 'yellow', 'orange'])
food.shape(shapes)
food.color(colors)
food.speed()
food.penup()
food.goto(100,0)

#score
pen = turtle.Turtle()
pen.shape('square')
pen.color('#000000')
pen.penup()
pen.goto(0,250)
pen.hideturtle()
pen.write('Score : 0  '    'High Score : 0', align='center'  ,font=('Arial' , 24 , 'bold'))
#movment_functions 
#up
def goup():
    if head.direction != 'down':
        head.direction = 'up'

#down
def godown():
    if head.direction != 'up':
        head.direction = 'down'
#right
def goright():
    if head.direction != 'left':
        head.direction = 'right'

#left
def godown():
    if head.direction != 'right':
        head.direction = 'left'

#move
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
            x = head.xcor()
            head.sety(x + 20)
    if head.direction == 'left':
            x = head.xcor()
            head.sety(x - 20)



#keyboard_keys
wn.listen()
wn.onkeypress(goup , 'Up')
wn.onkeypress(goup , 'Down')
wn.onkeypress(goup , 'Right')
wn.onkeypress(goup , 'Left')

def update_screen():
     wn.update()
     time.sleep(delay)


#main game loop 

while True :
     update_screen()