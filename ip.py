'''
    我的博客：https://darkabyss.top/ （求浏览量）
    功能：抓取国内高匿代理ip信息，抓取网址：https://www.kuaidaili.com/free/inha/1/
    描述：每次抓取会清除信息文件重新写入，有几页抓取不到，建议多给抓取页数
    已打包exe程序，下载地址：https://share.weiyun.com/5E6ivwr
'''

from lxml import etree
import requests
import os

try:
    os.remove("C:\\Users\\Administrator\\Downloads\\ip.txt")
except BaseException:
    pass
else:
    pass

edit = input("输入抓取页数(三千多页)：")
for i in range(int(edit)):
    i += 1
    res = requests.get('https://www.kuaidaili.com/free/inha/' + str(i) + '/')
    html = etree.HTML(res.text)
    jiedian = html.xpath('//tbody/tr')
    with open("C:\\Users\\Administrator\\Downloads\\ip.txt","a") as f1:
        f1.write("第" + str(i) + "页！" + "\n\n")
        print("抓取" + str(i) + "页！" + "\n")
    for j in jiedian:
        ip = "IP: " + j.xpath('./td[1]/text()')[0] + ":" + j.xpath('./td[2]/text()')[0] + "\n"
        ni = "匿名度：" + j.xpath('./td[3]/text()')[0] + "\n"
        typ = "类型：" + j.xpath('./td[4]/text()')[0] + "\n"
        wei = "位置：" + j.xpath('./td[5]/text()')[0] + "\n"
        send_time = "响应时间：" + j.xpath('./td[6]/text()')[0] + "\n"
        last = "最后验证时间：" + j.xpath('./td[7]/text()')[0] + "\n\n"
        j_list = ip + ni + typ + wei + send_time + last
        with open("C:\\Users\\Administrator\\Downloads\\ip.txt","a") as f:
            f.write(j_list)
            print("IP: " + j.xpath('./td[1]/text()')[0] + ":" + j.xpath('./td[2]/text()')[0])
    print('https://www.kuaidaili.com/free/inha/' + str(i) + '/')
print("抓取完成，请打开‘C:\\Users\\Administrator\\Downloads\\ip.txt’查看！")

