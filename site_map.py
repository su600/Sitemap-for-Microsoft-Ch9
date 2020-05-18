# -*- coding:utf-8 -*-
'''
    sitemap生成器，根据list生成 并非爬虫获取
    https://www.xml-sitemaps.com/ 效果比较理想
'''
import datetime
import re


# def get_url():
#     with open('D:\\Excel\\sitemap\\可用.txt', 'r', encoding='UTF-8') as f:
#         list1 = []
#         for i in f:
#             line = i.strip()
#             list1.append(line)

#         return list1


def creat_xml(filename, url_list):  # 生成sitemap所需要的xml方法
    header = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(header)
    file.close()

    for url in url_list:
        times = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        urls = re.sub(r"&", "&amp;", url)  # 注意这里,在URL中如果含有&将会出错,所以需要进行转义

        # 这个是生成的主体,可根据需求进行修改
        ment = "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n" % (urls, times)

        file = open(filename, 'a', encoding='utf-8')
        file.writelines(ment)
        file.close()

    last = "</urlset>"
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(last)
    file.close()


if __name__ == '__main__':
    # url_list = get_url()
    url_list = ['https://channel9.msdn.com/Series/More-Python-for-Beginners']
    creat_xml("D:/test1.xml", url_list)