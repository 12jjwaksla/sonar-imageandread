
# -*- coding: utf-8 -*-
import os,sys,time
fname=r"D:\01-学习资料\python"
def GetNowTime():#获取当前时间并以年月日时间方式显示
    return time.strftime("%m%d%H%M%S",time.localtime(time.time()))
#time=unicode(GetNowTime(),"utf8")
time=GetNowTime()
fname1=r"\t"+time+".txt" #设置根据当前时间动态命名txt文件，注意r主要用于特殊符号，因此r后需要存在特殊符号
fname+=fname1
t=open(fname.decode('utf8').encode('gbk'),'w')
t.write("你好吗111\n")

# -*- coding: utf-8 -*-
import os,sys,time
fname=r"D:\01-学习资料\python"
def GetNowTime():#获取当前时间并以年月日时间方式显示
    return time.strftime("%m%d%H%M%S",time.localtime(time.time()))
#time=unicode(GetNowTime(),"utf8")
time=GetNowTime()
fname1=r"\t"+time+".txt" #设置根据当前时间动态命名txt文件，注意r主要用于特殊符号，因此r后需要存在特殊符号
fname+=fname1
t=open(fname.decode('utf8').encode('gbk'),'w')
t.write("你好吗111\n")

t.close()