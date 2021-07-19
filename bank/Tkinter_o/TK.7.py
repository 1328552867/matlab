import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('1500x600')
#创建一个画布
canvas = tk.Canvas(window,bg='blue',height=500,width=1000)
#放置一张gif图片
image_file = tk.PhotoImage(file='1.gif')
#.create_image（位置，锚点，图片）
image = canvas.create_image(0,0,anchor='nw',image=image_file)
#定义坐标
x0,y0,x1,y1=50,50,100,100
#画直线，圆，扇形，正方形
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
rect = canvas.create_rectangle(200,30,220,50)
canvas.pack()
#移动正方形功能 每次向x轴移动0坐标向y轴移动5坐标
def moveit():
    canvas.move(rect,0,5)
b = tk.Button(window,text="move",command=moveit).pack()

#主窗口循环显示
window.mainloop()
