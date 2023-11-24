import tkinter as tk
from aip import AipSpeech
from pygame import mixer


def play():
    mixer.init()
    mixer.music.load('baidu.mp3')
    mixer.music.play()


def go_ai():
    mixer.quit()  # 每次点击按钮先清除mixer的加载
    words = e.get("1.0", "end")
    """ 你的 APPID AK SK """
    APP_ID = '40563296'
    API_KEY = 'C3S20pQyvmL8IzFPStvMGa2G'
    SECRET_KEY = 'A9VfLAb7Iu4CEoYhiOGNE9HfXg6eqA4d'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(words, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('baidu.mp3', 'wb') as f:
            f.write(result)
    play()


root = tk.Tk()
root.title('百度语音合成')
root.geometry('600x400+600+300')

# 安置在窗口;place主要帮你放置在上方下方左方右方这个几个位置
tk.Label(root, text="请输入文字：", bg="white").place(x=250, y=10)

# 设置一个文本框对象
e = tk.Text(root, width=50, height=17)
e.place(x=117, y=30)
# 设置按钮来完成功能
tk.Button(root, text='GO!', command=go_ai).place(x=275, y=260)

root.mainloop()
