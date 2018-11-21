# GUI编程，桌面程序
from tkinter import *

root = Tk()
li = [
    ".net",
    "java",
    "python",
    "go",
    "node.js"
]
lts = Listbox(root)
for e in li:
    lts.insert(0, e)
lts.pack()
# 进入消息循环
root.mainloop()
