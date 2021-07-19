
import turtle
#调用turtle库
def had (branch_length):
    count = 1
    #  计数
    while count <= 5:
        turtle.forward(branch_length)
        turtle.right(144)
        count = count + 1

def deaw_branch (branch_length):
    if branch_length > 20:

        #绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        if branch_length == 25:
            turtle.color('pink')
            had(branch_length)
            turtle.color('green')
        deaw_branch(branch_length - 15)

        #绘制左侧树枝
        turtle.left(40)
        deaw_branch(branch_length - 15)
        #返回之前树枝
        turtle.right(20)
        turtle.backward(branch_length)



def main ():
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('green')
    deaw_branch(100)

    turtle.up()
    turtle.goto(-300, 300)
    turtle.down()

    # 画出太阳的光芒，填充黄色
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(50, steps=8)
    turtle.end_fill()

    # 移动光标位置
    turtle.up()
    turtle.goto(-300, 300)
    turtle.down()

    # 画出一个圆，填充红色
    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(20)
    turtle.end_fill()


    turtle.exitonclick()

if __name__ == '__main__':
    main()
