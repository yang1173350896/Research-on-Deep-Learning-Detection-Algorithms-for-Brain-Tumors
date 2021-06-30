import colorsys
from PIL import Image
#改变图片颜色
#红
def trans_red(filename):
    # 输入文件
    filename = './static/images/output4/'+filename
    # 目标色值
    target_hue = 0/255
    # 读入图片，转化为 RGB 色值
    image = Image.open(filename).convert('RGB')
    # 将 RGB 色值分离
    image.load()
    r, g, b = image.split()
    result_r, result_g, result_b = [], [], []
    # 依次对每个像素点进行处理
    for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
        if (pixel_r >= 170 and pixel_g >= 170 and pixel_b >= 170):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
        #红
            pixel_r = 255
            pixel_g = 0
            pixel_b = 0
        result_r.append(pixel_r)
        result_g.append(pixel_g)
        result_b.append(pixel_b)
    r.putdata(result_r)
    g.putdata(result_g)
    b.putdata(result_b)
    # 合并图片
    image = Image.merge('RGB', (r, g, b))
    # 输出图片
    image.save('./static/images/output3/red.jpg')

#绿
def trans_lv(filename):
    # 输入文件
    filename = './static/images/output1/'+filename
    # 目标色值
    target_hue = 0/255
    # 读入图片，转化为 RGB 色值
    image = Image.open(filename).convert('RGB')
    # 将 RGB 色值分离
    image.load()
    r, g, b = image.split()
    result_r, result_g, result_b = [], [], []
    # 依次对每个像素点进行处理
    for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
        if (pixel_r >= 170 and pixel_g >= 170 and pixel_b >= 170):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
        #绿色
            pixel_r = 0
            pixel_g = 255
            pixel_b = 0

        result_r.append(pixel_r)
        result_g.append(pixel_g)
        result_b.append(pixel_b)
    r.putdata(result_r)
    g.putdata(result_g)
    b.putdata(result_b)
    # 合并图片
    image = Image.merge('RGB', (r, g, b))
    # 输出图片
    image.save('./static/images/output3/lv.jpg')