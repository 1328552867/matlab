

import turtle
#调用turtle库
def had (size):
    count = 1
    #  计数
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

def  draw_recursive_pentagram(size):
    """
        迭代绘制五角星
    """
    count = 1
    #  计数
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1
    size += 10
    if size <= 100:
        draw_recursive_pentagram(size)

def main ():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor('red')

    size = 50
    draw_recursive_pentagram(size)


    turtle.exitonclick()

if __name__ == '__main__':
    main()
