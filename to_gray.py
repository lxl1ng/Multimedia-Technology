import cv2


# 最大值法
def gray_max_rgb(inputimagepath, outimagepath):
    img = cv2.imread(inputimagepath)  # 读取图像，返回的是一个装有每一个像素点的bgr值的三维矩阵
    gray_max_rgb_image = img.copy()  # 复制图像，用于后面保存灰度化后的图像bgr值矩阵

    img_shape = img.shape  # 返回一位数组（高，宽，3）获得原始图像的长宽以及颜色通道数，一般彩色的颜色通道为3，黑白为1
    for i in range(img_shape[0]):  # 按行读取图片的像素bgr
        for j in range(img_shape[1]):  # 对每一行按照列进行每一个像素格子进行读取
            gray_max_rgb_image[i, j] = max(img[i, j][0], img[i, j][1], img[i, j][2])  # 求灰度值
    print(gray_max_rgb_image)

    cv2.imwrite(outimagepath, gray_max_rgb_image)  # 保存当前灰度值处理过后的文件


# 平均亮度法
def gray_avg_rgb(inputimagepath, outimagepath):
    img = cv2.imread(inputimagepath)
    gray_avg_rgb_image = img.copy()

    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            gray_avg_rgb_image[i, j] = (int(img[i, j][0]) + int(img[i, j][1]) + int(img[i, j][2])) / 3

    print(gray_avg_rgb_image)

    cv2.imwrite(outimagepath, gray_avg_rgb_image)  # 保存当前灰度值处理过后的文件


# 加权平均值法
def gray_weightmean_rgb(inputimagepath, outimagepath):
    wr = 0.30
    wg = 0.59
    wb = 0.11
    img = cv2.imread(inputimagepath)
    gray_weightmean_rgb_image = img.copy()

    img_shape = img.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            gray_weightmean_rgb_image[i, j] = (int(wr * img[i, j][2]) + int(wg * img[i, j][1]) + int(
                wb * img[i, j][0])) / 3
    print(gray_weightmean_rgb_image)

    cv2.imwrite(outimagepath, gray_weightmean_rgb_image)  # 保存当前灰度值处理过后的文件
