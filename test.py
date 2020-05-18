#coding=utf-8
# todo https://www.xml-sitemaps.com/ 生成xml
# todo 从sitemap.xml或html提取每一集的页面链接
# todo 从链接网页里获取视频和字幕地址
# todo 保存到excel中或者剪切板中
# todo 导入IDM批量下载

import urllib
import urllib.request 
import re
url='http://www.ranzhi.org/sitemap.xml'
html=urllib.request.urlopen(url).read()
html=html.decode('utf-8')
r=re.compile(r'(http://www.ranzhi.org.*?\.html)')
big=re.findall(r,html)
for i in big:
    print(i)
    op_xml_txt=open('xml.txt','a')
    op_xml_txt.write('%s\n'%i)