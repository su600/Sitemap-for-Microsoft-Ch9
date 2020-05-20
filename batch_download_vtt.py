'''
    下载字幕文件 并根据地址自动命名
    浏览器下载字幕文件有请求来获得文件名，IDM下载无文件名
    用Python程序截取下载连接中的文件名并下载
    将Vtt字符转换为srt字幕
'''
import requests
import pandas as pd
import os
# todo 更换目录 新建目录

urls = pd.read_excel('C:/Users/su514/Desktop/MIcrosoft More Python for Beginners/download_list222.xlsx')
urls = pd.DataFrame(urls)['英文字幕']

urls=urls.to_list()
for i in urls:
# print(urls['中文字幕'])
# url="https://channel9.msdn.com/Series/Even-More-Python-for-Beginners-Data-Tools/
# Demo-Visualizing-data-with-Matplotlib--Even-More-Python-for-Beginners-30-of-31/captions?f=webvtt&l=zh-cn"
    name = str(i).split('/ca')[0].split('/')[-1]+'.vtt'
    try:
        num = str(i).split('/ca')[0].split('-of-')[1]+'-'+str(i).split('/ca')[0].split('-of-')[0].split('-')[-1]+' '
        name = num+name
    except Exception as e:
        print(e)
    else:
        pass
    print(name)
    r=requests.get(i)

    with open(name,"wb") as f:
        f.write(r.content)
    f.close()

def traverseFolder(targetFolder):
    if(targetFolder[-1]==os.path.sep):
        targetFolder=targetFolder[0:-1]
    for root, dirs, files in os.walk(targetFolder):
        for oneFile in files:
            vtt2srt(root+os.path.sep+oneFile)

def vtt2srt(filePath):
    fileSplitName=os.path.splitext(filePath)
    if(fileSplitName[1]==".vtt"):
        print("Processing with file:    "+filePath)
        with open(filePath,"r",encoding="utf-8") as fin:
            fileContent=fin.readlines()
            lineNum=2
            fileMaxLineNum=len(fileContent)
            with open(fileSplitName[0]+".srt","w",encoding="gbk") as fout:
                fout.write("1\n")
                for i in range(2,fileMaxLineNum):
                    fout.write(fileContent[i].replace(".",","))
                    if(fileContent[i].strip()=="" and i+1<fileMaxLineNum and fileContent[i+1].strip()!=""):
                        fout.write(str(lineNum)+"\n")
                        lineNum+=1

# targetFolder= 'C:/Users/su514/Desktop/MIcrosoft More Python for Beginners/Videos/Even-More-Python-for-Beginners-Data-Tools'
# traverseFolder(targetFolder)


# #批量修改文件名
# #批量修改图片文件名
# import os
# import re
# import sys
# def renameall():
#     fileList = os.listdir(r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\More-Python-for-Beginners")		#待修改文件夹
#     print("修改前："+str(fileList))		#输出文件夹中包含的文件
#     currentpath = os.getcwd()		#得到进程当前工作目录
#     os.chdir(r"C:\Users\su514\Desktop\MIcrosoft More Python for Beginners\Videos\More-Python-for-Beginners")		#将当前工作目录修改为待修改文件夹的位置
#     # num=1		#名称变量
#     vtt=[]
#     video=[]
#     for fileName in fileList:		#遍历文件夹中所有文件
#         if 'captions' in fileName:
#             vtt.append(fileName)

#         if '.mp4' in fileName:
#             video.append(fileName)

#     print(video,vtt)

#     n=0
#     for i in vtt:
#         os.rename(i,(video[n].split('.')[0]+'.vtt'))		#文件重新命名
#         n+=1		#改变编号，继续下一项
#     print("---------------------------------------------------")
#     os.chdir(currentpath)		#改回程序运行前的工作目录
#     sys.stdin.flush()		#刷新
#     # print("修改后："+str(os.listdir(r"C:\Users\Administrator\Desktop\stars")))		#输出修改后文件夹中包含的文件


# renameall()

