from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import requests
import time

print('/////-✨-本脚本由PYS创建-✨-/////')
print('===按Ctrl+C结束运行===')

z = 0
page = int(input('===输入抓取起始页：'))
T_of_F = input('是否创建文件(''是''或''否'')：')
time.sleep(1)

if page == 1:
    print('===创建文件中===')
    time.sleep(1)
    os.makedirs('./img/',exist_ok=True)
    print('===创建成功===')
else:
    if T_of_F == '是':
        print('===创建''img''文件===')
        time.sleep(1)
        os.makedirs('./img/',exist_ok=True)
        print('===创建成功===')
    else:
        pass

for ss in range(int(input('===输入抓取页数：'))):
    page += 1
    htm = urlopen("https://wall.alphacoders.com/featured.php?lang=Chinese&page=" + str(page)).read().decode("utf-8")
    html = BeautifulSoup(htm,features="html.parser")
    all_a1 = html.find_all("div",{"class":"boxgrid"})
    print('\n')
    print('===开始下载图片===')
    print('\n')

    for i in all_a1:
        all_href = i.find_all("a")
        print('/')
        for l in all_href:
            all_url = l["href"]
            print('//')
            html1 = "https://wall.alphacoders.com/" + all_url
            print('///')
            html2 = urlopen(html1).read().decode("utf-8")
            print('////')
            text_html = BeautifulSoup(html2,features="html.parser")
            print('/////')
            all_a2 = text_html.find_all("picture")
            print('//////')

            for x in all_a2:
                all_img = x.find_all("img")
                print('///////')
                for s in all_img:
                    z += 1
                    img_url = s['src']
                    img_file = './img/img' + str(page*30+z-30) + '.png'
                    print('////////')
                    r = requests.get(img_url)
                    print('/////////')
                    with open(img_file,'wb') as f:
                        f.write(r.content)
                    print('===已下载第' + str(z) + '张图片')
    
    print('===已完成第' + str(page-1) + '页===\n')




