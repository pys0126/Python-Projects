import requests
import json
from datetime import datetime

#填写下面四个变量即可
#url为打卡的网址（就是分享链接），cookie从浏览器复制，name为你的名字，content是地址
url = "https://docs.qq.com/form/page/clock/DRlpWZnphd0ZrWElD?scene=0ad8e0604eafdb3d98313e99D29So1&_t=1630121607295#/fill-detail"
cookie = "RK=jzL0toKLTC; ptcz=317ac1fe39f6da0049b879fafbae26f120e99b6c50af83ade1745227a669f59e; _tc_unionid=1d2a621a-b787-47f6-b153-7c3f8eae162f; traceid=ca98778297; hashkey=ca987782; low_login_enable=1; vfwebqq=d53932b9752401c204a63d846a73869033d7ae97b138c9fd7efe0fbac97592cf6ae2fdbdc475ad16; docMessageCenterCookie=logout_144115213438861552; pgv_info=ssid=s562060251; pgv_pvid=24302876; ptui_loginuin=1637566997; uin=o1637566997; skey=@QJnpj9RP2; luin=o1637566997; lskey=000100004800ca20d45db0122c04a772c3ce419a566ddad5d61724a04184e147d698de9d2624d1d8882b62f5; p_uin=o1637566997; pt4_token=YUA5TZjNYPBoZRwfFXWzXM1NFJfswlQgYy-UGaQLjzY_; p_skey=mW2o8paEbTmJIKRVyAdEIZAivMh2ocmBw1mmzvUZ6kI_; p_luin=o1637566997; p_lskey=000400004da3d0495cfc6dc91e7091c37b90042948f5e4bdd3fe78d8e6e6adf282fbbe2e4598810f9c243bb9; TOK=15ee6d2ac442debc; has_been_login=1; uid=144115210466113323; utype=qq; uid_key=4%252FPD7m79urx0dPTLbdIG1HIdCfDITjDJBvr7Qr0GUO4t8HYlL%252BPqbPuwFR3QTiF9e8mnnTBt63lnRvCKjR%252BBAjfvgRS9SwOD"
name = "彭××"
content = "重庆市沙坪坝区双碑街道"

############################
session = requests.Session()
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://docs.qq.com",

}
cooki = {cookies.split(': ')[0]: cookies.split(': ')[1] for cookies in cookie.replace(";",",").replace("=", ": ").split(",")}
global_padid = {"global_padid":"300000000$FZVfzawFkXIC"}

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
                    "content": "h4xx0rz",
                    "dataType": 1
                }, {
                    "id": "time",
                    "type": "SIMPLE",
                    "content": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "dataType": 1
                }, {
                    "id": "lbs",
                    "type": "SIMPLE",
                    "content": "重庆市沙坪坝区双碑街道",
                    "dataType": 1
                }, {
                    "id": "select",
                    "type": "SELECT",
                    "content": "体温正常，身体健康",
                    "dataType": 1
                }, {
                    "id": "identity",
                    "type": "SIMPLE",
                    "content": "彭宇森",
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
    else:
        print(submit_re.text, "\n打卡成功")

if __name__ == "__main__":
    get_submit()




