import os
import imageio
import glob
import numpy as np
import time


# 生成中间帧
def generate_intermediate_frames(start_image_path, end_image_path, output_dir, num_frames):
    # 读取起始和结束图片
    time_start = time.time()  # 开始计时

    start_image = imageio.imread(start_image_path)
    end_image = imageio.imread(end_image_path)

    # 计算每一帧之间的差值
    diff = (end_image - start_image) / (num_frames + 1)
    output_path = os.path.join(output_dir, f"0.bmp")
    imageio.imwrite(output_path, start_image)
    # 生成中间帧并保存
    for i in range(num_frames):
        # 计算当前帧的图片
        current_frame = np.uint8(start_image + (i + 1) * diff)

        # 保存当前帧的图片
        output_path = os.path.join(output_dir, f"{i + 1}.bmp")
        imageio.imwrite(output_path, current_frame)
    print(f"{num_frames} intermediate frames generated and saved in {output_dir}")

    output_path = os.path.join(output_dir, f"21.bmp")
    imageio.imwrite(output_path, end_image)

    time_end = time.time()  # 结束计时

    time_c = time_end - time_start  # 运行所花时间
    print('time cost1', time_c, 's')


# 生成GIF
def to_gif(filename):
    # 静态图片存放路径，注意路径，否则找不到路径
    time_start = time.time()  # 开始计时
    filenames = glob.glob(filename)  # 遍历文件夹下的图片,注意后缀
    filenames = sorted(filenames, key=lambda x: int((os.path.basename(x).split('.')[0]).split('_')[-1]))
    print(filenames)
    # 转化的GIF图片名称
    save_name_gif = "generate.gif"

    # fps 就是图片切换的频率，越大越快。也可以使用duration参数来控制，表示每帧间隔，单位s
    duration = 0.2

    # 播放次数，0表示循环播放，1表示播放1次，2表示播放2次，以此类推
    loop = 0

    # 存放图片的列表
    pics_list = []

    # 遍历filenames,使用imageio读取后存入pics_list
    for image_name in filenames:
        im = imageio.imread(image_name)
        pics_list.append(im)

    # 生成gif
    imageio.mimsave(save_name_gif, pics_list, duration=duration, loop=loop)
    time_end = time.time()  # 结束计时

    time_c = time_end - time_start  # 运行所花时间
    print('time cost2', time_c, 's')
    return len(filenames)


file = './img' + '/*.bmp'
to_gif(file)
