import requests

class Htmldownloarder(object):

    def getresponse(self,page,time_from,time_to):    # 通过舞蹈专区获取UP的UID
        headers = {
            "Host": "s.search.bilibili.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.bilibili.com/v/dance/three_d/?spm_id_from=333.7.b_64616e63655f74687265655f64.1',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        link = "https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_19404339687289585&main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1\
        &cate_id=154&page="+str(page)+"&pagesize=20&jsonp=jsonp&time_from="+str(time_from)+"&time_to="+str(time_to)+"&_=1564412142733"

        # 这个link 是舞蹈专区最新发布视频的每个UP的个人UID
        r = requests.get(link,headers=headers)
        return r.text

    def photo_infrom(self,user_id):  #  获取照片的链接
        header = {
        "Accept":"*/*",
        "Host":"api.vc.bilibili.com",
        "Origin":'https://space.bilibili.com',
        "Referer":"https://space.bilibili.com/"+str(user_id)+"/album",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}
        link = 'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid='+str(user_id)+'&page_num=0&page_size=30&biz=all'
        r = requests.get(link,headers=header)
        return r.text
    
    def getphoto(self,link):
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Host':'i0.hdslb.com'
        }
        response = requests.get(link,headers=header)
        return response