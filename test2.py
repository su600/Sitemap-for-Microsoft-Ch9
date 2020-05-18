'''
    获取网页上的 High Quaklity MP4下载链接
    todo 获取本合集的所有视频网页 传递给当前程序
    todo 获取字幕文件
    todo 生成下载链接文件
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


import requests
from bs4 import BeautifulSoup
##########################################################################################
#coding=utf-8
import urllib
import urllib.request 

import re
url='https://channel9.msdn.com/sitemap.xml'
html=urllib.request.urlopen(url).read()
html=html.decode('utf-8')
r=re.compile(r'(https://channel9.msdn.com/Series/More-Python-for-Beginners.*?\.html)')
big=re.findall(r,html)
for i in big:
    print(i)
    op_xml_txt=open('xml.txt','a')
    op_xml_txt.write('%s\n'%i)
# print(op_xml_txt)
####################################################################################
def getHTMLText(url):
    '''
    此函数用于获取网页的html文档
    '''
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return '产生异常'

# def main():
'''
主函数
'''
#目标网页，这个可以换成一个你喜欢的网站
url = 'https://channel9.msdn.com/Series/More-Python-for-Beginners/Introducing-More-Python-for-Beginners--More-Python-for-Beginners-1-of-20'




demo = getHTMLText(url)

#解析HTML代码
soup = BeautifulSoup(demo, 'html.parser')

#模糊搜索HTML代码的所有包含href属性的<a>标签
# todo 根据标题筛选 提高效率
a_labels = soup.find_all('a', attrs={'href': True})
# a_labels = soup.find_all( string={'href': True})
#获取所有<a>标签中的href对应的值，即超链接
# todo 不用获取所有链接
download_list=[]
for a in a_labels:
    b=(a.get('href'))
    c=a.get_text()
    if 'High Quality MP4' in c or 'English' in c:
        # todo 文件格式
        download_list.append(c.strip())
        download_list.append(b.strip())

# list转dataframe
df = pd.DataFrame(download_list, columns=['downloadlist'])

# 保存到本地excel
df.to_excel("download_list.xlsx", index=False)

print( download_list)