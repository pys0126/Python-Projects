import requests
import json
from datetime import datetime

#填写下面四个变量即可
#url为打卡的网址（就是分享链接），cookie从浏览器复制，name为你的名字，content是地址
url = "填打卡地址"
cookie = "填cookie"
name = "填姓名"
qq_name = "填QQ名称" #QQ名称
global_padid = "填global_padid" #浏览器截取https://docs.qq.com/form/collect/recordcnt的请求data里面的global_padid
content = "填地址"

############################
session = requests.Session()
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://docs.qq.com",

}
cooki = {cookies.split(': ')[0]: cookies.split(': ')[1] for cookies in cookie.replace(";",",").replace("=", ": ").split(",")}
global_padid = {"global_padid": global_padid}

def role_id():
    role_id_re = session.post(url="https://docs.qq.com/form/collect/get_sign_role", headers=header, cookies=cooki, data=json.dumps(global_padid))
    if role_id_re.json()["code"] != 0:
        return "cookie可能过期了", quit
    return role_id_re.json()["selected_id"]

def get_submit():
    data = json.dumps({
            "global_padid": global_padid["global_padid"],
            "data": json.dumps([{
                    "id": "nick",
                    "type": "SIMPLE",
                    "content": qq_name,
                    "dataType": 1
                }, {
                    "id": "time",
                    "type": "SIMPLE",
                    "content": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "dataType": 1
                }, {
                    "id": "lbs",
                    "type": "SIMPLE",
                    "content": content,
                    "dataType": 1
                }, {
                    "id": "select",
                    "type": "SELECT",
                    "content": "体温正常，身体健康",
                    "dataType": 1
                }, {
                    "id": "identity",
                    "type": "SIMPLE",
                    "content": name,
                    "dataType": 1
                }]),
            "role": {
                "type": 1,
                "name": name,
                "role_id": role_id()
            }
        })
    submit_re = session.post(url="https://docs.qq.com/form/collect/submit", headers=header, data=data, cookies=cooki)
    if submit_re.json()["code"] == 10001:
        print(submit_re.text, "\n打卡失败")
    elif submit_re.json()["code"] == 18:
        print(submit_re.text, "\n已打卡")
    elif submit_re.json()["code"] == 0:
        print(submit_re.text, "\n打卡成功")
    else:
        print("global_padid可能不正确")

if __name__ == "__main__":
    get_submit()
