from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from to_gray import gray_max_rgb, gray_weightmean_rgb, gray_avg_rgb

root = Tk()
root.geometry('1200x650+170+100')
root.title('彩色图片灰度化')


def resize(w, h, pil_image):
    f1 = 1.0 * 250 / w
    f2 = 1.0 * 250 / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def choosepic():
    path_ = askopenfilename()
    path.set(path_)
    img_open = Image.open(file_entry.get())
    reimg = resize(img_open.width, img_open.height, img_open)
    img1 = ImageTk.PhotoImage(reimg)
    image_label1.config(image=img1)
    image_label1.image = img1  # keep a reference
    # result.config(text='dffffff')
    reimg.save("before.jpg")
    to_gray()


def to_gray():
    inputimagepath = "before.jpg"
    outimagepath1 = "gray_max_rgb.jpg"
    outimagepath2 = "gray_weightmean_rgb.jpg"
    outimagepath3 = "gray_avg_rgb.jpg"

    gray_max_rgb(inputimagepath, outimagepath1)
    gray_weightmean_rgb(inputimagepath, outimagepath2)
    gray_avg_rgb(inputimagepath, outimagepath3)


def show_grayimg():
    img_open2 = Image.open('gray_max_rgb.jpg')
    img_png2 = ImageTk.PhotoImage(img_open2)
    image_label2.config(image=img_png2)
    image_label2.image = img_png2

    img_open3 = Image.open('gray_avg_rgb.jpg')
    img_png3 = ImageTk.PhotoImage(img_open3)
    image_label3.config(image=img_png3)
    image_label3.image = img_png3

    img_open4 = Image.open('gray_weightmean_rgb.jpg')
    img_png4 = ImageTk.PhotoImage(img_open4)
    image_label4.config(image=img_png4)
    image_label4.image = img_png4


path = StringVar()  # 实时更新
Button(root, text='选择图片', command=choosepic).pack()
Button(root, text='GO!', command=show_grayimg).pack()

file_entry = Entry(root, state='readonly', text=path)
image_label1 = Label(root)
image_label1.place(x=470, y=60)
image_label2 = Label(root)
image_label2.place(x=100, y=350)
image_label3 = Label(root)
image_label3.place(x=470, y=350)
image_label4 = Label(root)
image_label4.place(x=840, y=350)
Label(root, text="最大值法", bg="white").place(x=200, y=325)
Label(root, text="平均值法", bg="white").place(x=570, y=325)
Label(root, text="加权法", bg="white").place(x=940, y=325)

root.mainloop()
