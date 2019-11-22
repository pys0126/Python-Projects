#导入模块
import requests
from bs4 import BeautifulSoup
#变量x用于生产完整网址
x = 100 #根据网址规律,图集是有序的,这是第20个图集,从这里开始,要修改也要修改第37行
print("\t----开始抓取----")
#定义一个函数，用于抓取单页
def page():   
    n = 0 #图集的第几张,一样有序,这是第一张图片
    while n < 10: #抓取图集前十张没有就跳过进行下一个图集的抓取
        n += 1 
        url = f'http://www.win4000.com/meinv{x}_{n}.html' #将变量x和n的数值插入以形成完整网址
        #header是为了解决反爬，让服务器以为是用浏览器访问的网址
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        data = requests.get(url,headers = header) #请求网址并解决反爬
        soup = BeautifulSoup(data.text,'lxml') #以文本格式列出网页所有信息
        #找出图片名称（titles）和图片的存在服务器的位置（imgs）
        titles = soup.select('div.ptitle > h1')
        imgs = soup.select('div.pic-meinv > a > img[url]')    

        #以拉链形式列出图片信息
        for title,img in zip(titles,imgs):
            data = {
                "title":list(title.stripped_strings), #以列表形式列出图片名称
                "img":img.get("url") #请求图片地址
            } 
            #存放在本机的文件名称,因为是图片,用 “.jpg” 形式存放
            filename = str(n) + data["title"][0] + ".jpg"
            pic = requests.get(data["img"])
            #以二进制写入 “.jpg” 文件
            with open('C:\\Users\\Administrator\\Downloads\\img\\' + filename,'wb') as photo:
                photo.write(pic.content)
            print("保存名：" + filename + "网址：" + data['img']) #从终端显示出图片已下载

#循环抓取各页的图集,并保存到 “ 下载/img ” 目录下
while x >= 100 and x < 150: 
    x += 1
    page()
print("\t----下载完成----")
print("已保存至：“C:\\Users\\Administrator\\Downloads\\img\\”目录")
    
















