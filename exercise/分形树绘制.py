
import turtle
#调用turtle库
def deaw_branch (branch_length):
    if branch_length > 20:

        #绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
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
    turtle.color('red')

    deaw_branch(100)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
