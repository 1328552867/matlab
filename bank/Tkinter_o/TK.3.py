import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('200x200')

var1 = tk.StringVar()

h = tk.Label(window,width=10,text="你喜欢谁？")
h.pack()
#Label 标签控件
l = tk.Label(window, bg='yellow',width=10,textvariable=var1)
l.pack()
def print_selection():
    #lb.curselection 获取光标指定的位置
    value = lb.get(lb.curselection())
    var1.set(value)

# 在窗口界面设置放置Button按键
b1 = tk.Button(window, text='print selection', font=('Arial', 12), width=10, height=1, command=print_selection)
b1.pack()
#定义插入列表的值
var2 = tk.StringVar()
var2.set(('迪丽热巴',22,33,44))
lb = tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
    lb.insert("end",item)
#lb.insert向列表插入（位置，数值）
lb.insert(1,"first")
lb.insert(2,"second")
#删除
lb.delete(2)
lb.pack()

#主窗口循环显示
window.mainloop()
