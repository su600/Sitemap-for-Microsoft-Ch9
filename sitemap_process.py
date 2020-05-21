'''
    打开sitemap文件 传递给当前程序
    获取每一集的网页地址
    解析每一集的高清视频地址和字幕地址
    格式化下载列表 分组
    生成下载链接文件
'''
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


import requests
from bs4 import BeautifulSoup

import urllib
import urllib.request
import re
import time


def getHTMLText(url):
    '''
    此函数用于获取网页的html文档
    '''
    try:
        # 获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout=6)
        # 判断返回状态码是否为200
        res.raise_for_status()
        # 设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        # 返回网页HTML代码
        return res.text
    except:
        return '产生异常'


# def main():
'''
主函数
'''

aa = 'C:/Users/su514/Desktop/MIcrosoft More Python for Beginners/sitemap.html'
# print('请输入sitemap.html文件路径')
# sitemap_path = input()
sitemap_path=aa
sitemap = open(sitemap_path, 'r')

# 解析sitemap
soup = BeautifulSoup(sitemap, 'html.parser')
print('正在解析sitemap文件')
# 模糊搜索HTML代码的所有包含href属性的<a>标签
# 提取 sitemap中的所有链接
a_labels = soup.find_all('a', attrs={'href': True})
# print('所有条目',a_labels)
#
print('正在分析所有链接')
link = []
# 解析所有链接
for i in a_labels:
    aa = i.get('href').strip()
    link.append((aa))

# print('所有链接',link)
title_list = []  # 标题
video__list = []  # 视频
subtitle_list1 = []  # 字幕 （英）
subtitle_list2 = []  # 字幕 （中）

print('正在提取链接')
for i in link:
    # 解析HTML代码
    demo = getHTMLText(i)
    soup = BeautifulSoup(demo, 'html.parser')
    # title = soup.find_all('a', attrs={'title': True})
    print(str(soup.find('title')))
    nn=(str(soup.find('title')).split('|')[0]+str(soup.find('title')).split('|')[1]).replace('<title>','')
    print(nn)
    title_list.append(nn)

    # 模糊搜索HTML代码的所有包含href属性的<a>标签
    # todo 根据标题筛选 提高效率
    a_labels = soup.find_all('a', attrs={'href': True})

    # 获取所有<a>标签中的href对应的值，即超链接
    # todo 不用获取所有链接
    # download_list=[]
    for a in a_labels:
        # print(a.get('title').strip())
        b = (a.get('href'))
        c = a.get_text()
        if 'High Quality MP4' in c:
            video__list.append(b.strip())

        elif 'English' in c:
            subtitle_list1.append(b.strip())

        elif '简体中文' in c:
            subtitle_list2.append(b.strip())
# print(title_list,video__list)
timenow = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

LL = [title_list, video__list, subtitle_list1,
      subtitle_list2]  # 所有的标题 视频地址 字幕地址打包
# list转dataframe
df = pd.DataFrame(LL)
df = df.T
df.rename(columns={0: 'title_list', 1: 'video__list',
                   2: '英文字幕', 3: '中文字幕'}, inplace=True)
# 保存到本地excel
filename = "download_list "+timenow+".xlsx"
df.to_excel(filename, index=False)
print('下载列表已保存到'+"download_list"+str(timenow)+".xlsx")

cb = pd.DataFrame(video__list)
cb.to_clipboard(index=False, header=False)
print('视频下载链接已复制到剪贴板，请使用下载软件(IDM)批量下载')

print('正在下载字幕文件')
'''
    下载字幕文件 并根据地址自动命名
    浏览器下载字幕文件有请求来获得文件名，IDM下载无文件名
    用Python程序截取下载连接中的文件名并下载
    将Vtt字符转换为srt字幕
'''
# todo 更换目录 新建目录

urls = subtitle_list1  # 英文字幕
for i in urls:
    name = str(i).split('/ca')[0].split('/')[-1]+'.srt'
    ## 直接修改扩展名为srt
    try:
        num = str(i).split('/ca')[0].split('-of-')[1]+'-' + \
            str(i).split('/ca')[0].split('-of-')[0].split('-')[-1]+' '
        name = num+name
    except Exception as e:
        print(e)
    else:
        pass
    
    # 下载字幕文件
    r = requests.get(i)

    with open(name, "wb") as f:
        f.write(r.content)
        f.close()

    ## 按srt格式转换
    with open(name, "r", encoding="utf-8") as fin:
        fileContent = fin.readlines()
        lineNum = 2
        fileMaxLineNum = len(fileContent)
        with open(name, "w", encoding="gbk") as fout:
            fout.write("1\n")
            for i in range(2, fileMaxLineNum):
                fout.write(fileContent[i].replace(".", ","))
                if(fileContent[i].strip() == "" and i+1 < fileMaxLineNum and fileContent[i+1].strip() != ""):
                    fout.write(str(lineNum)+"\n")
                    lineNum += 1
    print(name)

print('字幕已下载完成')