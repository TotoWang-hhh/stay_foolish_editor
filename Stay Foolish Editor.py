import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrtxt
import tkinter.messagebox as msgbox
import tkinter.filedialog as filebox
import sys


nowopen="none"


def openfile(path):
    global text,nowopen
    if path=='' or path==None:
        return
    nowopen=path
    f=open(path,'r',encoding='utf-8')
    text.delete(1.0,tk.END)
    filetxt=f.read()
    text.insert(tk.END,filetxt)
    f.close()

def savefile(path='nowopen'):
    global text,nowopen
    if path=='nowopen':
        path=nowopen
    if path=='none' or path=='choose':
        savefile(filebox.asksaveasfilename(title='保存文件',filetypes=[('文本文件','.txt'),('日志文件','.log'),('配置文件','.ini'),('所有文件','.*')]))
        return
    if path=='' or path==None:
        return
    f=open(path,'w',encoding='utf-8')
    f.write(text.get(1.0,tk.END))
    f.close()


if len(sys.argv)>1:
    openfile(sys.argv[1])

abouttxt='''Stay Foolish Editor
2023 By rgzz666 | v1.0.2
复刻参考：537文本编辑器v1.3
遵循Anti537许可

本编辑器默认使用支持中文的UTF-8

Stay Foolish Editor是537文本编辑器的复刻作品，
旨在证明537文本编辑器的制作成本低廉。

Stay Foolish Editor的取名取自537的座右铭
Stay Hungry, Stay Foolish的后半段，因为537只
做到了后半段的字面意思——当个傻子。

望537用心发展！'''

win=tk.Tk()
win.title('Stay Foolish Editor')

menu=tk.Menu(win)
filemenu=tk.Menu(menu)
filemenu.add_command(label='打开...',command=lambda:openfile(filebox.askopenfilename(title='打开文件',filetypes=[('文本文件','.txt'),('日志文件','.log'),('配置文件','.ini'),('所有文件','.*')])))
filemenu.add_command(label='保存',command=lambda:savefile())
filemenu.add_command(label='另存为...',command=lambda:savefile('choose'))
filemenu.add_command(label='退出',command=exit)
menu.add_cascade(label='文件',menu=filemenu)
menu.add_command(label='关于',command=lambda:msgbox.showinfo('关于',abouttxt))

win.config(menu=menu)

text=scrtxt.ScrolledText(win)
text.pack(fill=tk.BOTH,expand=True)

win.mainloop()
