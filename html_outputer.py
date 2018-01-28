# coding:utf-8
from urllib import request
import os

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self,data):
        if data is None:
            return None
        self.datas.append(data)
    def output_html(self):
        src = "d://img/"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
        for data in self.datas:
            i=1
            try:
                src = "d://img/"+data['alt']+"/"
                isExists=os.path.exists(src)
                if not isExists:
                    os.makedirs(src)
                    for d in data['lst']:
                        #print ('src %s url:%s' % (src,d))
                        req = request.Request(url=d, headers=headers)  
                        feeddata = request.urlopen(req).read()  
                        #print (feeddata)
                        f=open(src+data['alt']+str(i)+'.jpg','wb')
                        print ('src %s' % (src+data['alt']+str(i)+'.jpg'))
                        i=i+1  
                        f.write(feeddata)  
                        #urllib.request.urlretrieve(d,src+data['alt'])
            except:
                print('faild')
