#  关于B站舞蹈区的UP主相簿下载的一个小软件
#
#   Version 1.0.1
#
#   需要继续完善的功能：
#   1、通过在下载目录以每个UP主的MID命名的文件夹，识别是否已下载这个UP的图片
#   2、添加可选参数：页数page、时间参数time_from与time_to
#   3、设置多线程 
#   4、添加代理池
#
from Htmldownloader import Htmldownloarder
from HtmlParse import HtmlParse
class SpiderMain(object):
    def __init__(self):
        self.crawl = Htmldownloarder()
        self.jsondata = HtmlParse()

    def run(self):
        page = '1'
        time_from = '20190722'
        time_to = '20190729'
        response = self.crawl.getresponse(page,time_from,time_to) # 
        user_list = self.jsondata.parse(response)
        # 拿到用户id之后就可以请求相册内容了
        for each in user_list:
            user_photo_response = self.crawl.photo_infrom(each) 
            self.jsondata.photo_parse(user_photo_response)


    
spider = SpiderMain()
spider.run()