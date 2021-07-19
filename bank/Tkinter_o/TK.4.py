import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('400x400')
var = tk.StringVar()
l = tk.Label(window, width=20, text="作出你的选择")
l.pack()
def print_selection():
    l.config(text="you have selected" + var.get())
#tk.Radiobutton生成选择 把value赋值给variable
r1 = tk.Radiobutton(window,text='迪丽热巴',variable=var,value="A",command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window,text='范冰冰冰',variable=var,value="B",command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window,text='李小龙   ',variable=var,value="C",command=print_selection)
r3.pack()
#主窗口循环显示
window.mainloop()
