import re
import csv
import threading
import time
import requests
from fake_useragent import UserAgent


# 定义一个爬虫类
class AbstractSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        with open('paper0.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            self.url_list = [row[1] for row in reader]

    # 请求函数
    def get_html(self, url, index):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        res = requests.get(url, headers)
        res.encoding = "utf-8"
        html = res.text
        self.parse_html(html, index)

    # 解析函数
    def parse_html(self, html, index):
        # 正则表达式
        # re_bds = '"title":"(.*?)".*?"full_name":"(.*?)".*?"has_code".*?"url":"(.*?)".*?"publication_date":"(.*?)"'
        re_bds = '<div class="authors">.*?<span class=.*?<span ' \
                 'class="author-span">(.*?)</span>.*?<div class="paper' \
                 '-abstract">.*?<p>\n            (.*?)\n        </p>'
        # 生成正则表达式对象
        obj_info_list = re.compile(re_bds, re.S)
        # info_list: [('title','url','date')...] 列表元组
        info_list = obj_info_list.findall(html)
        author = ''
        abstract = ''
        if len(info_list) > 0:
            temp_info = info_list[0]
            author = temp_info[0]
            abstract = temp_info[1]
            if '</a>' in author:
                author = author[author.find('>') + 1:author.find('</a>')]
            if '\n                                    ' in author:
                author = author[len('\n                                    '):]
            abstract = abstract.replace('\n', ' ')
        info = (author, abstract)
        self.save_html(info, index)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, info, index):
        # 生成文件对象
        file_name = 'abstract0.csv'
        with open(file_name, 'a', newline='', encoding="utf-8") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            author = info[0]
            abstract = info[1]
            row = [author, abstract, index + 1]
            # 写入csv文件
            writer.writerow(row)

    # 主函数
    def run(self):
        count = 7592

        while count < len(self.url_list):
            '''if count % 20 == 0:
                time.sleep(random.uniform(1, 2))'''
            self.get_html(self.url_list[count], count)
            count = count + 100

    # 以脚本方式启动
    # 捕捉异常错误

    def process(self):
        t1 = time.time()

        t_list = []
        for i in range(100):
            t = threading.Thread(target=AbstractSpider.run, args=(self, i))
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

        print("多线程版爬虫耗时：", time.time() - t1)


try:
    spider = AbstractSpider()
    spider.process()
except Exception as e:
    print("错误:", e)
