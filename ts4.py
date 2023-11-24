import imageio
import os
import numpy as np


def generate_intermediate_frames(start_image_path, end_image_path, output_dir, num_frames):
    # 读取起始和结束图片
    start_image = imageio.imread(start_image_path)
    end_image = imageio.imread(end_image_path)

    # 计算每一帧之间的差值
    diff = (end_image - start_image) / (num_frames + 1)
    output_path = os.path.join(output_dir, f"s.bmp")
    imageio.imwrite(output_path, start_image)
    # 生成中间帧并保存
    for i in range(num_frames):
        # 计算当前帧的图片
        current_frame = np.uint8(start_image + (i + 1) * diff)

        # 保存当前帧的图片
        output_path = os.path.join(output_dir, f"frame{i + 1}.bmp")
        imageio.imwrite(output_path, current_frame)
    print(f"{num_frames} intermediate frames generated and saved in {output_dir}")

    output_path = os.path.join(output_dir, f"e.bmp")
    imageio.imwrite(output_path, end_image)


start_image_path = '起始帧1.bmp'
end_image_path = '终止帧1.bmp'
output_dir = './img'
num_frames = 20
generate_intermediate_frames(start_image_path, end_image_path, output_dir, num_frames)
