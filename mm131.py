'''
    爬取的网站为：https://www.mm131.pro/e/action/ListInfo/?classid=1
    另外此脚本我已打包成了EXE程序，就是像用电脑QQ一样，一个按钮就可以享受视觉盛宴，那么下载地址：https://share.weiyun.com/5lkhNxS
    如果此脚本对你有帮助😁，可以访问我的网站：https://darkabyss.top 里面有一些翻墙知识，如果你不想看也可以大致浏览一下，我需要你的流量，Thanks!
'''


from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import requests
import os

p = -1
cc = 4
print("\t本脚本由P=-S编写，有建议或问题致QQ：2493919891\n")

for c in range(cc):
    cc -= 1
    int_page = input("\t输入抓取的页数（一页25套图片）：")
    if int_page == "":
        print("\t请输入一个整数,你还有" + str(cc) + "次机会！")
        pass
    else:
        break

cc = 4
for c in range(cc):
    cc -= 1
    page = input("\t输入抓取的页数（一页25套图片）：")
    if page == "":
        print("\t请输入一个整数,你还有" + str(cc) + "次机会！")
        pass
    else:
        break


for i in range(int(page)):
    p += 1
    html = urlopen("https://mm131.pro/e/action/ListInfo/index.php?page=" + str(int_page+p) + "&classid=1").read()
    soup = BeautifulSoup(html,features="lxml")
    dl_soup = soup.find_all("dl",{"class":"list-left public-box"})
    print("\t开始下载...\n")
    for ssp in dl_soup:
        dd_soup = ssp.find_all("dd")[:-1]
        for ddp in dd_soup:
            dd_href = ddp.find_all("a")
            for a_href in dd_href:
                all_href = "https://mm131.pro" + a_href["href"]
                all_title = a_href.find_all("img")
                img = 0
                for dir_name in all_title:
                    img += 1
                    dir_img = dir_name["alt"]
                    all_dir = "mm131/" + dir_img
                    os.makedirs(all_dir,exist_ok=True)
                all_html = urlopen(all_href).read()
                all_soup = BeautifulSoup(all_html,"lxml")
                page_url = all_soup.find_all("div",{"class":"content-pic"})
                for all_page in page_url:
                    page_href = all_page.find_all("a")
                    pageone_img = all_page.find_all("img")
                    for one_alt in pageone_img:
                        oneall_alt = one_alt["alt"]
                        oneimg_url = one_alt["src"]
                        rurl = requests.get(oneimg_url)
                        one_name = str(all_dir) + "/"+ str(oneall_alt) + ".jpg"
                        with open(one_name,"wb") as sf:
                            sf.write(rurl.content)
                        print(one_name)
                    page_size = all_soup.find("span",{"class":"page-ch"})
                    size = int(page_size.get_text()[1:-1])
                    for pageone in page_href:
                        pageone_url = pageone["href"]
                        ints = 1
                        for all_int in range(size-1):
                            ints += 1
                            allpage_url = "https://www.mm131.pro" + pageone_url[:-7] + "_" + str(ints) + ".html" 
                            size_url = urlopen(allpage_url).read()
                            size_html = BeautifulSoup(size_url,"lxml")
                            htmls = size_html.find_all("div",{"class":"content-pic"})
                            for size_h in htmls:
                                tag_img = size_h.find_all("img")
                                tag_alt = size_h.find_all("alt")
                                for all_src in tag_img:
                                    src = all_src["src"]
                                    alt = all_src["alt"]
                                    r = requests.get(src)
                                    save_name = str(all_dir) + "/" + str(alt) + ".jpg"
                                    with open(save_name,"wb") as f:
                                        f.write(r.content)
                                    print("\t" + save_name)
                print("\t已下载" + str(img) + "套图\n")
    print("\t已下载" + str(page) + "页图片\n")


                        

                        
                        



                
                


