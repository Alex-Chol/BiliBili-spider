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
            #'Cookie': "buvid3=974B876A-024A-4868-B018-6792A44E9B97110232infoc; LIVE_BUVID=AUTO7615588815523138; sid=6qpfxzm9; UM_distinctid=16af49a44d49-0ab6dc9fe4dccc-4c312d7d-1fa400-16af49a44d51dc; fts=1558882006; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(J|~|YJlllu0J'ullmkJ|)Ym; DedeUserID=77657138; DedeUserID__ckMd5=985cfe51e46000dc; SESSDATA=10246f4c%2C1564458331%2Cb6385d61; bili_jct=30f9ba2e28ed92007be33c4bfb067649; _ga=GA1.2.1670068456.1562728586",
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