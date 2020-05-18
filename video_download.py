
#   _*_ coding:utf-8 _*_
from urllib import request
from bs4 import BeautifulSoup
__author__ = 'admin'
 
#   目标网站地址
url = "https://channel9.msdn.com/Series/More-Python-for-Beginners/Introducing-More-Python-for-Beginners--More-Python-for-Beginners-1-of-20"
#   构造报文头信息，模拟浏览器登录无需输入用户名密码的网站
headers = {
    #   下面为360浏览器的header中User-Agent信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
#   url请求，返回request对象
page = request.Request(url=url, headers=headers)
#   打开网址
page_info = request.urlopen(page).read().decode('utf-8')
#   格式化网页
print(page_info)
soup = BeautifulSoup(page_info, 'html.parser')
#   搜索页签为"a"的匹配项
contents = soup.find_all('a')
for content in contents:
    if content.string == '摩托卖场':
        print(content.string)
        print(content.get('href'))
    elif content.string == '相机':
        print(content.string)
        print("http://gz.58.com/" + content.get('href'))
    elif content.string == '加菲猫':
        print(content.string)
