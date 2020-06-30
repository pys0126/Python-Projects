# coding=utf-8
'''
    抓取网址：https://mm603.xyz
    需要的依赖库：lxml和requests,在cmd用 pip install [库名称] 安装依赖库
'''

from lxml import etree
import requests
import os
import re

class Av:
    #请求头
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    #初始化
    def __init__(self,types,path,url="https://mm603.xyz/search.php?key=",heade=header):
        self.types = types
        self.url = url
        self.heade = heade
        self.path = path
        os.makedirs(path+"av\\"+types,exist_ok=True)   #在给出的路径创建文件夹     

    def down_av(self):
        rq = requests.get(self.url+self.types,headers=self.heade) #请求搜索的目标网站
        html = etree.HTML(rq.text) 
        video_url = html.xpath('//div[@class="pic"]/ul/li/a/@href') #搜索结果各视频的链接
        video_name = html.xpath('//div[@class="pic"]/ul/li/a/text()') #搜索结果各视频的名称
        x = -1

        for vu in video_url:
            x += 1
            one_rq = requests.get("https://mm603.xyz"+vu,headers=self.heade) #请求视频所在网页
            one_html = etree.HTML(one_rq.text)
            one_data = one_html.xpath('//source/@src')[2] #找出视频源地址
            res = requests.get(one_data,headers=self.heade)
            #将视频名称的空格去掉
            r = re.compile(r'\S')
            li = r.findall(video_name[x])
            name = ''.join(li) #最终的视频名称
            #保存视频
            with open(self.path+"av\\"+self.types+"\\"+name+".mp4","wb") as f:
                f.write(res.content)
            print("已下载"+name+".mp4")

sea = input("输入你想要的内容：")
pa = input("输入保存的路径：")
#Av([搜索想要内容]，[保存路径如：'C:\\Users\\Administrator\\Downloads\\'])
run = Av(sea,pa)
run.down_av()
