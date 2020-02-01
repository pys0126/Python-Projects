'''
    此程序下载地址：https://share.weiyun.com/52J7qi2
    我的其他脚本：https://github.com/pys0126/Python/
    如果此脚本对你有帮助，可以访问我的网站：https:darkabyss.top 我需要你的流量，Thanks!
'''

import requests
import tkinter as tk

#创建中文翻译函数
def fanyizh():
    data = {
        "i": tt.get(0.0,"end"),
        "from": "en",
        "to": "zh-CHS",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15487335011539",
        "sign": "d821abc9357326f21054a6d05760e8b4",
        "ts": "1548733501153",
        "bv": "363eb5a1de8cfbadd0cd78bd6bd43bee",
        "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
    }
    res = requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",data)
    ls = res.json()["translateResult"][0][0]['tgt']
    tt.delete(0.0,"end")
    tt.insert("end",ls)

#创建英文翻译函数
def fanyien():
    data = {
        "i": tt.get(0.0,"end"),
        "from": "zh-CHS",
        "to": "en",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15487335011539",
        "sign": "d821abc9357326f21054a6d05760e8b4",
        "ts": "1548733501153",
        "bv": "363eb5a1de8cfbadd0cd78bd6bd43bee",
        "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
    }
    res = requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",data)
    ls = res.json()["translateResult"][0][0]['tgt']
    tt.delete(0.0,"end")
    tt.insert("end",ls)

#创建清除文本函数
def col():
    tt.delete(0.0,"end")

#创建窗口
start = tk.Tk()
start.title("翻译")
start.geometry("400x200")

#创建一个标题和输入框
ll = tk.Label(start,text="请输入翻译内容：")
ll.grid()
tt = tk.Text(start,width=56,height=7)
tt.grid()

#创建三个按钮并插入函数
zh = tk.Button(start,text="中文翻译",width=8,command=fanyizh)
zh.grid(row=2,column=0)
en = tk.Button(start,text="英文翻译",width=8,command=fanyien)
en.grid(row=3,column=0)
de = tk.Button(start,text="清除",width=8,command=col)
de.grid(row=4,column=0)

#循环刷新窗口
start.mainloop()

