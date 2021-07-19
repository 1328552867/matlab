import tkinter as tk
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('500x300')
tk.Label(window,text='on the window').pack()
#在window上创建一个Frame
frm = tk.Frame(window)
frm.pack()
#设置一左一右两个框架
frm_l = tk.Frame(frm,)
frm_r = tk.Frame(frm,)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l,text='on the frm_l').pack()
tk.Label(frm_r,text='on the frm_r').pack()
tk.Label(frm_l,text='on the frm_l').pack()
#主窗口循环显示
window.mainloop()
