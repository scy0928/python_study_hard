#turtle이라는 모듈을 사용할 건데, turtle, Screen 클래스를 import할겁니다.
from turtle import Turtle, Screen

t= Turtle()        #Turtle클래스의 객체 생성, 이름은 t
screen = Screen()  #Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# t.penup()
# t.forward(100)
# t.pendown()
# t.forward(200)
#
# for _ in range(10):     #그냥 반복을 10번하는 것도 변수를 사용하지 않았기 때문에 그냥 _를 씀( i나 n이 아니라)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)




screen.exitonclick()


