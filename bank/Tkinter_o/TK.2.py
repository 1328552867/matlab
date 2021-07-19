import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('1300x800')

e = tk.Entry(window,show="")
e.pack()
def insert_point():
    var = e.get()
    #.insert(填充位置，填充内容)  "insert"插入到指针指到的位置
    t.insert('insert',var)
def insert_end():
    var = e.get()
    # "end"插入到指针指到的位置
    t.insert('end',var)

# 在窗口界面设置放置Button按键
b1 = tk.Button(window, text='insert point', font=('Arial', 12), width=10, height=1, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', font=('Arial', 12), width=10, height=1, command=insert_end)
b2.pack()

t = tk.Text(window,height=2)
t.pack()
#主窗口循环显示
window.mainloop()
