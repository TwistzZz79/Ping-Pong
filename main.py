from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle= Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()

    

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")



game_is_on=True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()
    
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
        ball.speed-=0.03
    
    if ball.xcor()>420:
        ball.reset()
        scoreboard.increase_l_score()
        
    if ball.xcor()<-420:
        ball.reset()
        scoreboard.increase_r_score()


screen.exitonclick()