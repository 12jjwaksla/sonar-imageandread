from PIL import Image
import math
import binascii
import numpy as np
a1=[]
a2=[]
count=1
def A(data):#把数据拼成图片的函数,和图像数据不同的是，每组数据会产生两长条图片，一个高频一个低频
    global count
    b=[]
    i=0
    for i in range(0,len(data),4):#先按照小端读取数据尝试读取
        b.append(int((ping_channel1Data[i+2:i+4]+ping_channel1Data[i:i+2]),16))
    #print(len(b))
    Gmax=max(b)
    Gmin=min(b)
    #print(Gmax)
    #print(Gmin)
    j=0
    a=[]
    for j in range(0,len(b)-1,1):
        a.append(int((b[j]-Gmin)*255/(Gmax-Gmin)))#将声波强度数据转换为灰度图数据，16位转8位
    width=len(b)
    height=1
    # 创建一个新的灰度图像对象
    image = Image.new("L", (width, height))
    # 将灰度数据赋值给图像的像素
    image.putdata(a)
    # 显示图像
    image.save(str(count)+".bmp")
    if count%2==1:
        a1.append('./'+str(count)+'.bmp')#左频图像
    if count%2==0:
        a2.append('./'+str(count)+'.bmp')#右频图像
    count+=1
with open('E:\\桌面\\all\\大型auv声呐实验\\sonardata\\0816 202254raw.txt', 'r')as f:
    while True:
        data=f.readline()
        if not data:
            break
        data1=bytes(data[29:-2].encode())
        xtf_header=data1[:2048]
        xtf_SonarChannel=xtf_header[332:336]
        Channel=int((xtf_SonarChannel[2:4]+xtf_SonarChannel[0:2]),16)
        if Channel>6:
            xtf_header=xtf_header+data[2048:4096]
        data_channel1=xtf_header[512:768]
        data_channel2=xtf_header[768:1024]
        data_channel3=xtf_header[1024:1280]
        data_channel4=xtf_header[1280:1536]
        data_channel5=xtf_header[1536:1792]
        data_channel6=xtf_header[1792:2048]
        Channel1_BytesPerSample=data_channel1[12:16]
        BytesPerSample1=int((Channel1_BytesPerSample[2:4]+Channel1_BytesPerSample[0:2]),16)
        Channel2_BytesPerSample=data_channel2[12:16]
        BytesPerSample2=int((Channel2_BytesPerSample[2:4]+Channel2_BytesPerSample[0:2]),16)
        ping1header=data1[2048:2560]
        chan1head=data1[2560:2688]
        channelhead_NumSam=chan1head[84:92]
        NumSam1=int((channelhead_NumSam[6:8]+channelhead_NumSam[4:6]+channelhead_NumSam[2:4]+channelhead_NumSam[0:2]),16)
        Chan1_Bytes2=NumSam1*BytesPerSample1
        ping_channel1Data=data[2688:2688+Chan1_Bytes2*2]
        A(ping_channel1Data)
        chan2head=data[2688+Chan1_Bytes2*2:2688+Chan1_Bytes2*2+128]
        channe2head_NumSam=chan2head[84:92]
        NumSam2=int((channelhead_NumSam[6:8]+channelhead_NumSam[4:6]+channelhead_NumSam[2:4]+channelhead_NumSam[0:2]),16)
        Chan2_Bytes2=NumSam2*BytesPerSample1
        ping_channel2Data=data[2688+Chan1_Bytes2*2+128:2688+Chan1_Bytes2*2+128+Chan2_Bytes2*2]
        A(ping_channel2Data)
img_array1 = ''
img1= ''
for i, v in enumerate(a1):#左频图像纵向拼接
    if i == 0:
        img1= Image.open(v)  # 打开图片
        img_array1 = np.array(img1)  # 转化为np array对象
    if i > 0:
        img_array2 = np.array(Image.open(v))
        #img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        img_array1 = np.concatenate((img_array1, img_array2), axis=0)  # 纵向拼接
        img1 = Image.fromarray(img_array1)
        img1=img1.rotate(180)
img1.save('left.bmp')
img_array21= ''
img2= ''
print((i))
for y, z in enumerate(a2):#右频图像纵向拼接
    if y == 0:
        img2 = Image.open(z)  # 打开图片
        img_array21 = np.array(img2)  # 转化为np array对象
    if y > 0:
        img_array2 = np.array(Image.open(z))
        #img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        img_array21 = np.concatenate((img_array21, img_array2), axis=0)  # 纵向拼接
        img2 = Image.fromarray(img_array21)
#print(a2)
img2.save('right.bmp')
a3=['./left.bmp','./right.bmp']
img_array3=''
img3=''
for i, v in enumerate(a3):#左右合并
    if i == 0:
        img3 = Image.open(v)  # 打开图片
        img_array3 = np.array(img3)  # 转化为np array对象
    if i > 0:
        img_array2 = np.array(Image.open(v))
        img_array3 = np.concatenate((img_array3, img_array2), axis=1)  # 横向拼接
        #img_array3 = np.concatenate((img_array3, img_array2), axis=0)  # 纵向拼接
        img3 = Image.fromarray(img_array3)
img3.save('final.bmp')
