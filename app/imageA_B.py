import cv2 as cv
#将图片A与B融合
def image_lv_and_red(filename):
    #输出地址
    file_dir = './static/images/output3/'+filename

    img1 = cv.imread('./static/images/output3/red.jpg')
    img2 = cv.imread('./static/images/output3/lv.jpg')
    # 在lena.png获取和logo.png大小相同的ROI
    rows, cols, channels = img1.shape
    img_ROI1 = img2[0:rows, 0:cols]

    # 将两幅图像（lena.png）+ (logo.png)进行融合
    img2 = cv.imread('./static/images/output3/lv.jpg')
    # 1，在lena.png获取和logo.png大小相同的ROI
    img_ROI1 = img2[0:rows, 0:cols]

    # 2，基于logo.png的灰度图，利用简单的阈值分割创建一个掩模
    img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img1_gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)

    # 3，与掩模进行按位与操作，去掉logo中非0部分，得到新的图
    new_img2 = cv.bitwise_and(img_ROI1, img_ROI1, mask=mask_inv)

    # 4，将新图与logo相加，然后将这一部分替换掉原始图像的img_ROI1部分
    dst = cv.add(img1, new_img2)
    img2[0:rows, 0:cols] = dst

    cv.imwrite(file_dir,img2)


