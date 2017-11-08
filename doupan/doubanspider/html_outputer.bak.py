import os
import urllib

class HtmlOutputer(object):

    def __init__(self,):
        self.data = []
        # self.url = url

    def collect_data(self, new_data):
        self.data.append(new_data)

    def output(self,newdata):
        file = open('douban.txt', 'w', encoding='utf-8')

        if newdata in  self.data:

            for item in newdata:
                self.save_images(item)
                self.save_text(file,item)
        # for arr in self.data:
        #     for item in arr:
        #         self.save_text(file, item)
        #         self.save_images(item)

        file.close()

        print('Done~')


    def save_text(self, file, item):

        file.write(item['index'] + '  ' + item['title'])
        file.write('\n')

    def save_images(self, item):
        if os.path.exists('pics') == False: # 如果不存在创建这个文件甲A
            print('mkdir pics')
            os.mkdir('pics')
        # 拼接文件名
        filename = item['index'] + "-" + item['title'] + os.path.splitext(item['pic'])[1]
        resource = urllib.request.urlopen(item['pic'])
        data = open('pics/%s' % filename, 'wb')
        data.write(resource.read())
        data.close()
        print('Saved %s' % filename)

