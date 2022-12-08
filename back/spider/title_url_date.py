import re
import csv
import threading
import time
import requests
from fake_useragent import UserAgent


# 定义一个爬虫类
class UrlSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://paperswithcode.com/api/internal/papers/?page='

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
        re_bds = '"title":"(.*?)".*?"has_code".*?"url":"(.*?)".*?"publication_date":"(.*?)"'
        # 生成正则表达式对象
        obj_info_list = re.compile(re_bds, re.S)
        # info_list: [('title','url','date')...] 列表元组
        info_list = obj_info_list.findall(html)
        self.save_html(info_list, index)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, info_list, index):
        # 生成文件对象
        file_name = 'paper' + str(index % 5) + '.csv'
        with open(file_name, 'a', newline='', encoding="utf-8") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            # 整理数据
            for info in info_list:
                title = info[0]
                # author = info[1]
                url = 'https://paperswithcode.com' + info[1]
                date = info[2]
                row = [title, url, date]
                # 写入csv文件
                writer.writerow(row)

    # 主函数
    def run(self, index):
        count = index
        while count < 107600:
            '''if count % 20 == 0:
                time.sleep(random.uniform(1, 2))'''
            self.get_html(self.url + str(count), index)
            count = count + 400
            # self.get_html(self.next_url)

    # spider = PaperSpider()
    # spider.run()

    # 以脚本方式启动
    # 捕捉异常错误

    def process(self):
        t1 = time.time()

        t_list = []
        for i in range(100):
            t = threading.Thread(target=UrlSpider.run, args=(self, i))
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

        print("多线程版爬虫耗时：", time.time() - t1)


spider = UrlSpider()
spider.process()
