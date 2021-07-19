import tkinter as tk
import tkinter.messagebox
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('500x300')
tk.Label(window,text=1).pack(side="top")
tk.Label(window,text=1).pack(side="bottom")
tk.Label(window,text=1).pack(side="left")
tk.Label(window,text=1).pack(side="right")

# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j,padx=10)
tk.Label(window,text=1).place(x=10,y=100,anchor="nw")
#主窗口循环显示
window.mainloop()
