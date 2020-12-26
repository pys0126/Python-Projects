# 好壁纸下载
from bs4 import BeautifulSoup
import requests
import getpass
import time
import re
import os

start_time = time.time()  #获取开始时间
user_name = getpass.getuser()  #获取当前计算机用户名
search = input("输入搜索内容：")  
start_size = input("输入起始页：")
stop_size = input("输入结束页：")
stop = int(stop_size) - int(start_size)

#下载图片函数
def download(ss,sh=search):
    url = f"http://m.bcoderss.com/tag/{sh}/page/{ss}/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    error = soup.title.text
    if re.match("404",error):
        print("搜索内容不存在，请重新运行！")
        quit()
    else:
        li = soup.find("ul",class_="wallpaper").find_all("li")
        for l in li:
            img_url = l.a["hresf"]
            res_iu = requests.get(img_url)
            soup_iu = BeautifulSoup(res_iu.text,"lxml")
            img_title = soup_iu.find("div",class_="single-wallpaper")["pageid"]
            img_url = soup_iu.find("div",class_="single-wallpaper").img["src"]
            get_img = requests.get(img_url)
            try:
                with open(f"C:\\Users\\{user_name}\\Picturess\\img\\"+img_title+".jpg","wb") as f:
                    f.write(get_img.content)
            except:
                try:
                    os.mkdir(f"C:\\Users\\{user_name}\\Picturess\\img")
                except:
                    pass
            print(img_title)
        print("完成"+"第"+str(ss)+"页！")

#运行。。。
if int(stop_size) == 1:
    download(start_size)
else:
    while True:
        if int(start_size) == int(stop_size):
            break
        elif int(start_size) == 0:
            print("输入错误，请重新运行！")
            break
        else:
            download(start_size)       
            start_size = int(start_size) + 1

#记录时间
stop_time = time.time()
print("用时："+str(stop_time - start_time))
        



