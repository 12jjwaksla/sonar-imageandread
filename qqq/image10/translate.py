from PIL import Image
import math
import binascii
import numpy as np
a1=[]
with open('E:\\桌面\\大型auv声呐实验\\sonardata\\0816 203519image.txt', 'r') as f:#要这样打开文件才能从头读到尾
    count=1#用来表示文件名的变量，同时也可以看with循环了多少次，和文件内的数据是否对应
    while True:
        data = f.readline()#切记读取文件和接收数据不一样，读取文件永远默认是string类型
        if not data:
            break
        data1 = bytes(data[29:-2].encode())#由于是string类型，所以切分数据的时候要把b和'一切切掉，末尾还有换行符，所以末尾也要多切掉一个
        b = len(data1)
        header = data1[:256]
        rgbdata = data1[256:]
        Width1 = header[32:36]
        Height1 = header[36:40]
        Width2 = Width1[0:2]
        Width3 = Width1[2:4]
        Width = int((Width3 + Width2), 16)
        Height2 = Height1[0:2]
        Height3 = Height1[2:4]
        Height = int((Height3 + Height2), 16)
        im = Image.new("RGB", (Width, Height))
        k = 0
        for i in range(0, Height):
            for j in range(0, Width):
                im.putpixel((j, i), (int(rgbdata[6 * k:6 * k + 2], 16), int(rgbdata[6 * k + 2:6 * k + 4], 16), int(rgbdata[6 * k + 4:6 * k + 6], 16)))
                k += 1
        im.save(str(count) + '.bmp')
        a1.append('./'+str(count)+'.bmp')
        count+=1
img_array = ''
img = ''
for i, v in enumerate(a1):
    if i == 0:
        img = Image.open(v)  # 打开图片
        img_array = np.array(img)  # 转化为np array对象
    if i > 0:
        img_array2 = np.array(Image.open(v))
        #img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        img_array = np.concatenate((img_array, img_array2), axis=0)  # 纵向拼接
        img = Image.fromarray(img_array)
img.save('final.jpg')
