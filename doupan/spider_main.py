# coding=utf-8
from doupan.doubanspider import html_downloader,html_outputer,html_parser
from  doupan.doubanspider.myThread import MyThread
from doupan.doubanspider.timer import timer
from bs4 import BeautifulSoup

import os
import encodings.idna
import time,datetime
import json



class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, new_url):
        html_cont = self.downloader.download(new_url)
        new_data = self.parser.parse_data(html_cont)
        self.outputer.collect_data(new_data)


@timer
def  main():
    obj_spider = SpiderMain()

    threads = []
    number=20
    for i in range(0, number):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % (i * 25)
        # print(url)
        t = MyThread(obj_spider.crawl, (url,),name=obj_spider.crawl.__name__,)
        threads.append(t)
        # threads[i].daemon=False
        threads[i].start()


    for i in range(0,number):
        threads[i].join()


    # print('len:',len(obj_spider.outputer.data))

    # 写入到文件，保存img
    # obj_spider.outputer.output()

    # 把数据写成json 格式




      #     # json.dump(obj_spider.outputer.data,fp=fp,indent=4,ensure_ascii=False)






'''
  
    for item in obj_spider.outputer.data:
        # print(item)
        # print(type(item))
        with open('douban.json', 'a') as fp:
            json.dump(item, fp=fp, indent=4, ensure_ascii=False)
 '''


if __name__ == "__main__":

    main()

    # os.system("pause")
