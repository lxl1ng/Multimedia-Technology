import tkinter as tk
from tkinter import filedialog
from ts3 import *

window = tk.Tk()
window.title('图像变换动画')
window.geometry('1280x680')

tk.Label(window, text="起始帧文件路径：").place(x=320, y=20)
var_name = tk.StringVar()  # 文件输入路径变量

tk.Label(window, text="终止帧文件路径：").place(x=320, y=50)
var_name2 = tk.StringVar()  # 文件夹输入路径变量

entry_name = tk.Entry(window, textvariable=var_name, width=55)
entry_name.place(x=420, y=20)
entry_name2 = tk.Entry(window, textvariable=var_name2, width=55)
entry_name2.place(x=420, y=50)


def select_files1():
    path_ = filedialog.askopenfilename()
    var_name.set(path_)


def select_files2():
    path_ = filedialog.askopenfilename()
    var_name2.set(path_)


def show():
    start_image_path = entry_name.get()
    end_image_path = entry_name2.get()
    output_dir = './img'
    num_frames = 20
    # 生成中间帧
    generate_intermediate_frames(start_image_path, end_image_path, output_dir, num_frames)
    num = to_gif('./img' + '/*.bmp')
    play_gif(num)


def play_gif(num):
    numIdx = num  # gif的帧数
    # 填充内容到frames
    # 读取gif路径
    frames = [tk.PhotoImage(file='generate.gif', format='gif -index %i' % (i)) for i in range(numIdx)]

    def update(idx):  # 定时器函数
        frame = frames[idx]
        idx += 1  #
        label.configure(image=frame)  # 显示当前帧的图片
        window.after(200, update, idx % numIdx)  # 0.2秒(200毫秒)之后继续执行定时器函数(update)

    window.after(0, update, 0)  # 立即启动定时器函数(update)


tk.Button(window, text="起始帧路径", command=select_files1).place(x=825, y=15)
tk.Button(window, text="终止帧路径", command=select_files2).place(x=825, y=45)
tk.Button(window, text="GIF生成", command=show).place(x=600, y=75)
label = tk.Label(window)
label.place(x=280, y=150)

window.mainloop()
