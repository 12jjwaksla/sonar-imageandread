# -*- coding: utf-8 -*-
from PIL import Image
import math
import binascii
f=open('E:\\桌面\\大型auv声呐实验\\sonardata\\0816 202747image.txt','r')
while True:
    data=f.readline()#读取进来的是字符串格式。需要变成16进制
    data1=bytes(data[29:-2].encode())#把时间去掉
    b=len(data1)
    header=data1[:256]
    rgbdata=data1[256:]
    Width1=header[32:36]
    Height1=header[36:40]
    #print(b)
    #print(len(header))
    #print(len(rgbdata))
    #print(Width1)
    #print(Height1)
    Width2=Width1[0:2]
    Width3=Width1[2:4]
    Width=int((Width3+Width2),16)#最终宽度
    #print(Width)
    Height2=Height1[0:2]
    Height3=Height1[2:4]
    Height=int((Height3+Height2),16)#最终高度
    im = Image.new("RGB", (Width, Height)) 
    k=0;
    j=0;
    for i in range (0,Height):#像素是竖着排列的
        for j in range(0,Width):
       # im.putpixel((j,i),int(rgbdata[6*k,6*k+2]),16),int(rgbdata[6*k+2:6*k+4],16),int(rgbdata[6*k+4:6*k+6],16)
            im.putpixel((j, i), (int(rgbdata[6*k:6*k+2],16), int(rgbdata[6*k+2:6*k+4],16), int(rgbdata[6*k+4:6*k+6],16)))#记录第几个数据点
            k=k+1
        im.save(str(j)+'.bmp')
f.close()


