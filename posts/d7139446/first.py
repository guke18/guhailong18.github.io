import imageio


def create_gif(image_list, gif_name, duration=1):
    """
    :param image_list: 原始图片，png
    :param gif_name: gif的文件名
    :param duration: 间隔时间
    path：路径
    :return:
    """

    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # 保存为GIF
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)

    return


def main():
    image_list = ['1.png', '2.png', '3.png', '4.png']
    gif_name = 'first.gif'
    duration = 1.5
    create_gif(image_list, gif_name)


# 当前程序被当作主程序运行时， __ name__被自动赋值为固定的字符串__main__;当它被当作模块被其他文件调用时，自动被赋值为模块所在的文件名
if __name__ == '__main__':
    main()