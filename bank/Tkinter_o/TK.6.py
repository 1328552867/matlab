"""
2020/9/22
tk 图形化
"""
import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('500x300')

l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()
def print_selection():
    if(var1.get()==1) and (var2.get()==0):
        l.config(text='I love only Python')
    elif(var1.get()==0) and (var2.get()==1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) and (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()




#主窗口循环显示
window.mainloop()
