import turtle
# -- coding:utf-8 --
#画三角形
import turtle
turtle.pensize(5)
turtle.pencolor('red')
turtle.circle(100,720)





def draw(m):
    n=1
    a=180-((m-2)*180/m)
    while n<=m:
        turtle.forward(20)
        turtle.right(a)
        n=n+1

"""

draw(3)
draw(6)
draw(15)
draw(60)
"""


turtle.mainloop()