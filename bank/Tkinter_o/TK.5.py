import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小pyinstaller
window.geometry('400x400')
var = tk.StringVar()
l = tk.Label(window, width=20, text="作出你的选择",bg='yellow')
l.pack()
def print_selection(v):
    l.config(text="you have selected" + v)
'''设置进度条 label显示上方文本 from_ to设置范围 orient设置进度条方向 length长度 showvalue实时显示滑块旁边上的数值
tickinterval设置刻度 resolution设置精度'''
s = tk.Scale(window,label='try me',from_=5,to=11,
             orient=tk.HORIZONTAL,length=200,showvalue=0,
             tickinterval=3,resolution=0.01,command=print_selection)
s.pack()



#主窗口循环显示
window.mainloop()
