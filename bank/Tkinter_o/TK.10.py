import tkinter as tk
import tkinter.messagebox
#建立窗口window
window = tk.Tk()
#给窗口可视化起名
window.title('这是一个窗口')
#设定窗口的大小
window.geometry('500x300')

def hit_me():
    #提示信息
    #tk.messagebox.showinfo(title='Hi',message="hh 我是信息")
    #提示错误
    #tk.messagebox.showerror(title='Hi', message="hh 我是错误")
    #提示警告
    #tk.messagebox.showwarning(title='Hi', message="hh 我是警告")
    #提示选择 返回 yes no
    #tk.messagebox.askquestion(title='Hi', message="你是天下最帅的人？")
    # 提示选择 返回 Ture False
    tk.messagebox.askyesno(title='Hi', message="你是天下最帅的人？")
    #重试/取消对话框 askretrycancel 是/否/取消对话框 askyesnocancel  确认/取消对话框 askokcancel



tk.Button(window,text='HIT ME',command=hit_me).pack()
#主窗口循环显示
window.mainloop()
