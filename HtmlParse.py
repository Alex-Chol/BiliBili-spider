import json,re,requests
from urllib import request
from Htmldownloader import Htmldownloarder

class HtmlParse(object):
    def __init__(self):
        self.download_photo = Htmldownloarder()
    def parse(self,response):
        if response:
            response_text = response
            key = re.compile(r"jqueryCallback_bili_\d+\(")
            result1 = key.findall(response_text)
            r = response_text.replace(result1[0],"")
            r = r.replace(")","")
            datas = json.loads(r)
            result = datas['result']
            print(result)
            user_id = []
            for i in range(0,len(result)):
                user_id.append(result[i]['mid'])
            return user_id
        elif response == 'null':
            return "response is null"
        else:
            return "response unknow error"
    
    def photo_parse(self,response):
        path = 'D://Bilibili_picture/'
        if response:
            datas = json.loads(response)
            result = datas['data']['items']
            #photo_link_list = []
            for each in range(0,len(result)):
                a = 1
                name = result[each]['description']
                print(name)
                print("此相册共有"+str(result[each]['count'])+'张照片')
                for each_photo in range(0,len(result[each]['pictures'])):
                    link = result[each]['pictures'][each_photo]['img_src'] 
                    # 图片的链接
                    res = self.download_photo.getphoto(link)  # 调用下载图片函数进行下载图片数据
                    with open(path+name+str(a)+'.jpg','wb') as f: # 保存到本地
                        f.write(res.content)
                        f.close()
                    a += 1



            
        
