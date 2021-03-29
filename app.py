import turtle
import random
import time


delay = 0.1
score = 0
heighestScore = 0

totalBody = []

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("white")
s.setup(height=600, width=600)


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("pink")
food.penup()
food.hideturtle()
food.goto(0, 200)
food.showturtle()


sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.hideturtle()
sb.goto(-250, -250)
sb.write("Score: 0 | Heighest Score: 0")

def moveup():
    if head.direction!="down":
        head.direction = "up"

def movedown():
    if head.direction!="up":
        head.direction = "down"


def moveleft():
    if head.direction!="right":
        head.direction = "left"

def moveright():
    if head.direction!="left":
        head.direction = "right"   

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)     


s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")


while True:
    s.update()

    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)    

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        totalBody.append(body)

        score+= 1
        delay-= 0.001

        if score > heighestScore:
            heighestScore = score
        sb.clear()
        sb.write("Score: {} Highest Score: {}".format(score, heighestScore))    
                    


    for i in range(len(totalBody)-1, 0, -1):
        x = totalBody[i-1].xcor()
        y = totalBody[i-1].ycor()
        totalBody[i].goto(x, y)

    if len(totalBody) > 0:
        x = head.xcor()
        y = head.ycor()
        totalBody[0].goto(x, y)
    move()    

    for body in totalBody:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in totalBody:
                body.hideturtle()
            totalBody.clear()

            score = 0
            delay = 0.1

            sb.clear()
            sb.write("Score: {} Highest Score: {}".format(score, heighestScore))   

    time.sleep(delay)
s.mainloop()

















