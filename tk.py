from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title('彩色图像灰度化')
root.geometry('1280x600')

img1 = Image.open('2.jpeg')
img1 = img1.resize((200, 200))
photo1 = ImageTk.PhotoImage(img1)
label_img1 = Label(root, image=photo1)
label_img1.grid(row=1, column=0, pady=10)

img2 = Image.open('gray_max_rgb.jpg')
img2 = img2.resize((200, 200))
photo2 = ImageTk.PhotoImage(img2)
label_img2 = Label(root, image=photo2)
label_img2.grid(row=1, column=1, pady=10)

img3 = Image.open('gray_avg_rgb.jpg')
img3 = img3.resize((200, 200))
photo3 = ImageTk.PhotoImage(img3)
label_img3 = Label(root, image=photo3)
label_img3.grid(row=1, column=2, pady=10)

img4 = Image.open('gray_weightmean_rgb.jpg')
img4 = img4.resize((200, 200))
photo4 = ImageTk.PhotoImage(img4)
label_img4 = Label(root, image=photo4)
label_img4.grid(row=1, column=3, pady=10)

root.mainloop()
