#turtle이라는 모듈을 사용할 건데, turtle, Screen 클래스를 import할겁니다.
import random
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

# for _ in range(4):
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(90)
# for _ in range(3):
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(120)


def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

# #삼각형도 그려볼까요?
# for _ in range(3):
#     dotted_line()
#     t.left(120)
#
# #이상의 함수를 사용하여 사각형을 그린다고 가정했을 때
#
# for _ in range(4):
#     dotted_line()
#     t.left(90)
#
# #해당 부분까지 다 한신 분들은
# #오각형, 육각형 ... 십각형까지 그려볼 수 있게 하고
# #이후 코드를 축약할 방법까지 고민해보도록 하겠습니다.
#
# for _ in range(5):
#     dotted_line()
#     t.left(72)



def draw_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360/num)

#랜덤 객체를 생성
random = random.Random()


colors = ["indian red", "cyan", "medium slate blue", "medium blue", "gold",
          "medium spring green", "snow", "peru", "dodger blue", "medium blue",
          "light green", "dark red", "tomato", "chocolate", "lime green"] #내부에 거북이 색깔을 요소로 하는 리스트를 생성
    #랜덤 모듈을 사용하세요(행맨에서 했습니다)

# t.color(" indian red ")


for i in range(3,11,1):
    draw_figures(i)
    t.color(random.choice(colors))

screen.exitonclick()


