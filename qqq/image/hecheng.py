import numpy as np
 
from PIL import Image
paths = ['./0.bmp','./1.bmp', './2.bmp', './3.bmp', './4.bmp','./5.bmp','./6.bmp','./7.bmp','./8.bmp','./9.bmp' ,
         './10.bmp', './11.bmp','./12.bmp', './13.bmp', './14.bmp','./15.bmp','./16.bmp','./17.bmp','./18.bmp','./19.bmp',
         './20.bmp','./21.bmp', './22.bmp', './23.bmp', './24.bmp','./25.bmp','./26.bmp','./27.bmp','./28.bmp','./29.bmp',
         './30.bmp','./31.bmp', './32.bmp', './33.bmp', './34.bmp','./35.bmp','./36.bmp','./37.bmp','./38.bmp','./39.bmp',
         './40.bmp','./41.bmp', './42.bmp', './43.bmp', './44.bmp','./45.bmp','./46.bmp','./47.bmp','./48.bmp','./49.bmp',
         './50.bmp','./51.bmp', './52.bmp', './53.bmp', './54.bmp','./55.bmp','./56.bmp','./57.bmp','./58.bmp','./59.bmp',
         './60.bmp','./61.bmp', './62.bmp', './63.bmp', './64.bmp','./65.bmp','./66.bmp','./67.bmp','./68.bmp','./69.bmp',
         './70.bmp','./71.bmp', './72.bmp', './73.bmp', './74.bmp','./75.bmp','./76.bmp','./77.bmp','./78.bmp','./79.bmp',
         './80.bmp','./81.bmp', './82.bmp', './83.bmp', './84.bmp','./85.bmp','./86.bmp','./87.bmp','./88.bmp','./89.bmp',
         './90.bmp','./91.bmp', './92.bmp', './93.bmp', './94.bmp','./95.bmp','./96.bmp','./97.bmp','./98.bmp','./99.bmp',
         './100.bmp','./101.bmp', './102.bmp', './103.bmp', './104.bmp','./105.bmp','./106.bmp','./107.bmp','./108.bmp','./109.bmp',
         './110.bmp','./111.bmp', './112.bmp', './113.bmp', './114.bmp','./115.bmp','./116.bmp','./117.bmp','./118.bmp','./119.bmp',
         './120.bmp','./121.bmp', './122.bmp', './123.bmp', './124.bmp','./125.bmp','./126.bmp','./127.bmp','./128.bmp','./129.bmp',
         './130.bmp','./131.bmp', './132.bmp', './133.bmp', './134.bmp','./135.bmp','./136.bmp','./137.bmp','./138.bmp','./139.bmp',
         './140.bmp','./141.bmp', './142.bmp', './143.bmp', './144.bmp','./145.bmp','./146.bmp','./147.bmp','./148.bmp','./149.bmp',
         './150.bmp','./151.bmp', './152.bmp', './153.bmp', './154.bmp','./155.bmp','./156.bmp','./157.bmp','./158.bmp','./159.bmp',
         './160.bmp','./161.bmp', './162.bmp', './163.bmp', './164.bmp','./165.bmp','./166.bmp','./167.bmp','./168.bmp','./169.bmp',
         './170.bmp','./171.bmp', './172.bmp', './173.bmp', './174.bmp','./175.bmp','./176.bmp','./177.bmp','./178.bmp','./179.bmp',
         './180.bmp','./181.bmp', './182.bmp', './183.bmp', './184.bmp','./185.bmp','./186.bmp','./187.bmp','./188.bmp','./189.bmp',
         './190.bmp','./191.bmp', './192.bmp', './193.bmp', './194.bmp','./195.bmp','./196.bmp','./197.bmp','./198.bmp','./199.bmp',
         './200.bmp','./201.bmp', './202.bmp', './203.bmp', './204.bmp','./205.bmp','./206.bmp','./207.bmp','./208.bmp','./209.bmp',
         './210.bmp','./211.bmp', './212.bmp', './213.bmp', './214.bmp','./215.bmp','./216.bmp','./217.bmp','./218.bmp','./219.bmp',
         './220.bmp','./221.bmp', './222.bmp', './223.bmp', './224.bmp','./225.bmp','./226.bmp','./227.bmp','./228.bmp','./229.bmp',
         './230.bmp','./231.bmp', './232.bmp', './233.bmp', './234.bmp','./235.bmp','./236.bmp','./237.bmp','./238.bmp','./239.bmp',
         './240.bmp','./241.bmp', './242.bmp', './243.bmp', './244.bmp','./245.bmp','./246.bmp','./247.bmp','./248.bmp','./249.bmp',
         './250.bmp','./251.bmp', './252.bmp', './253.bmp', './254.bmp','./255.bmp','./256.bmp','./257.bmp','./258.bmp','./259.bmp',
         './260.bmp','./261.bmp'
         ]
img_array = ''
img = ''
for i, v in enumerate(paths):
    if i == 0:
        img = Image.open(v)  # 打开图片
        img_array = np.array(img)  # 转化为np array对象
    if i > 0:
        img_array2 = np.array(Image.open(v))
        #img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        img_array = np.concatenate((img_array, img_array2), axis=0)  # 纵向拼接
        img = Image.fromarray(img_array)
 
 
 
# 保存图片
img.save('final.jpg')
