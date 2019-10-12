from PIL import Image

# 现将input image 填充为正方形
def fill_imag(image):
    width,height=image.size
    # 选取长和宽中拉伸值作为新图片
    new_image_length =(width if width>=height else height)
    # 生成新图片[白底]
    new_image = Image.new(image.mode,
                          (new_image_length,new_image_length),
                          color='pink')
    # 将之前的图粘贴在新图上,居中
    if width>height:
        # 原图宽度大于高,则填充图片的垂直维度
        # #(y,x)二元组表示粘贴上图相对下图的起始位置,是个坐标点
        new_image.paste(image,(0,int((new_image_length-height)/2)))
    else:
        new_image.paste(image,(0,int((new_image_length-width)/2)))
    return new_image

# 分割图片int((new_image_length-(height/2))
def cut_image(image):
    width,height=image.size
    item_width=int(width/3)
    box_list=[]# (left, upper, right, lower)
    for i in range(3):
        for j in range(3):
            box = (j * item_width,
                   i * item_width,
                   (j + 1) * item_width,
                   (i + 1) * item_width)
            box_list.append(box)
    return [image.crop(box) for box in box_list]

# 保存图片
def save_image(image_list):
    index = 1
    for image in image_list:
        image.save(str(index)+'.png','PNG')
        index += 1

if __name__ == '__main__':
    # 获取要进行分割的图片路径
    image1 = Image.open("wzry2.jpeg")
    image = fill_imag(image1)
    image_list = cut_image(image)
    save_image(image_list)

